from odoo import models, fields, api, tools


class Photograph(models.Model):
    _name = 'website_keith.photograph'

    name = fields.Char("Title", required=True)
    featured = fields.Boolean("Featured")
    category_ids = fields.Many2many('website_keith.photograph.category',
                                    'photograph_category_rel',
                                    'photograph',
                                    'category',
                                    'Category', required=True)
    image = fields.Binary("Photo", required=True, attachment=True)

    # Scaled Images
    image_medium = fields.Binary(string="Medium-sized image",
                                 store=False,
                                 compute="_get_image",
                                 help="Medium-sized image of this model. It is automatically " \
                                      "resized as a 128x128px image, with aspect ratio preserved. " \
                                      "Use this field in form views or some kanban views.")

    image_small = fields.Binary(string="Small-sized image",
                                store=False,
                                compute="_get_image",
                                help="Small sized image of this model. It is automatically " \
                                     "resized as a 64x64px image, with aspect ratio preserved. " \
                                     "Use this field in form views or some kanban views.")

    sequence = fields.Integer("Sequence")
    notes = fields.Text("Notes")

    @api.one
    @api.depends("image")
    def _get_image(self):
        """ calculate the images sizes and set the images to the corresponding
            fields
        """
        image = self.image

        # check if the context contains the magic `bin_size` key
        if self.env.context.get("bin_size"):
            # refetch the image with a clean context
            image = self.env[self._name].with_context({}).browse(self.id).image

        data = tools.image_get_resized_images(image)
        self.image_medium = data["image_medium"]
        self.image_small = data["image_small"]
        return True


class PhotographCategory(models.Model):
    _name = 'website_keith.photograph.category'

    name = fields.Char("Name", required=True)
    photograph_ids = fields.Many2many(
        "website_keith.photograph",
        "photograph_category_rel",
        'category',
        'photograph',
        string="Photos")
