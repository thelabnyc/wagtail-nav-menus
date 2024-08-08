# Changes

## v3.10

- Add support for Wagtail 4.0.x, 4.1.x., 4.2.x, and 5.0.x.

## v3.9

- Add support for Wagtail 3.

## v3.8

- Nav menu choices now customizable
- Can now add choices to Nav Categories exclusively

## v3.7

- Add Wagtail 2.16 support

## v3.6

- Add Wagtail 2.13 support


## v3.5

- Add Wagtail 2.12 support

## v3.4

- Add Wagtail 2.11 support

## v3.3

Thanks @jaap3 for everything in this release

- Add wagtail 2.10 support
- Fix bug that caused unnecessary migrations to be created

## v3.2

- Add wagtail 2.9 support

## v3.1

- Added Abstract model for NavMenu to make extensions easier

## v3.0

- Potentially breaking change - added Site foreign key to nav menus to enable different menus per site. Migration will attempt to set this new required field to the default wagtail site.
- Added optional rest framework serializer
- Added optional rest framework viewset

## v2.0

Breaking change - support wagtail 2.x. For wagtail 1.x use version 1.1.

## v1.1

added "menu_name" context variable to template tag
