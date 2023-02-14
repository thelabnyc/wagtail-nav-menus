.PHONY: translations

# Create the .po and .mo files used for i18n
translations:
	cd src/wagtail_nav_menus && \
	django-admin makemessages -a && \
	django-admin compilemessages

makemigrations:
	docker-compose run web python sandbox/manage.py makemigrations
