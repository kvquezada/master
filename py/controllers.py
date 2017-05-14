from odoo import http, models, api, exceptions, tools
from odoo.addons.website.controllers.main import Website
from odoo.http import request
import requests


class WebsiteKeith(http.Controller):
    @http.route('/gallery.json', auth='public', type='json', website=True)
    def get_institution(self, **kw):
        env = request.env
        institution_model = env['website_lvem.institution_template']
        institution_ids = institution_model.search([], limit=8)
        return {
            'institutions': [
                {
                    'id': institution_id.id,
                    'name': institution_id.name,
                    'image': institution_id.image,
                    'image_gray': institution_id.image_gray
                }
                for institution_id in institution_ids]
        }

    @http.route('/news-events.json', auth='public', type='json', website=True)
    def get_news_events(self):
        env = request.env
        blog_post_model = env['blog.post']
        latest_news_ids = blog_post_model.search([], order='post_date desc', limit=3)
        return {
            'news': [
                {
                    'id': latest_news_id.id,
                    'name': latest_news_id.name,
                    'content': latest_news_id.content,
                    'post_date': latest_news_id.post_date,
                } for latest_news_id in latest_news_ids],
        }

    @http.route('/category.json', auth='public', type='json', website=True)
    def get_category(self, **kw):
        env = request.env
        category_model = env['website_lvem.category']
        category_ids = category_model.search([], )
        return {
            'categories': [
                {
                    'id': category_id.id,
                    'name': category_id.name,
                    'family_categories': [{
                                              'id': family_id.id,
                                              'child_name': family_id.name,
                                              'parent_id': family_id.parent_id.id,
                                              'parent_name': family_id.parent_id.name,
                                          } for family_id in category_id.child_id]
                } for category_id in category_ids],
        }

    @http.route(['/lvem/quote', ], auth='public', type='http', methods=["POST"], website=True)
    def lvem_quote_request(self, **post):
        env = request.env
        # Validate form recaptcha
        g_recaptcha_response = None
        gcaptcha_secret = http.request.env['website'].browse(1)[0].recaptcha_private_key
        try:
            g_recaptcha_response = requests.post(
                url="https://www.google.com/recaptcha/api/siteverify",
                params={
                    'secret': gcaptcha_secret,
                    'response': post.get('g-recaptcha-response')
                })
        except Exception:
            pass
        # Continue...
        if g_recaptcha_response and g_recaptcha_response.json().get('success') or post.get('_b'):
            pass

    # lvem5 page route
    @http.route('/lvem-technology-and-design', auth='public', type='http', website=True)
    def render_technology_and_design_page(self, **post):
        return request.render('website_lvem.technology_and_design')

    @http.route('/LVEM5-benchtop-tem', auth='public', type='http', website=True)
    def render_lvem5_tem_page(self, **post):
        return request.render('website_lvem.lvem5_tem')

    @http.route('/lvem5-benchtop-transmission-electron-microscope-tem-boost', auth='public', type='http', website=True)
    def render_tem_boost_page(self, **post):
        return request.render('website_lvem.tem_boost')

    @http.route('/LVEM5-benchtop-sem', auth='public', type='http', website=True)
    def render_sem_page(self, **post):
        return request.render('website_lvem.sem')
