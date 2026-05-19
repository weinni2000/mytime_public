{
    "name": "Date Form Advanced Widget",
    "summary": "Adds a website page for the advanced date form widget.",
    "version": "18.0.1.1.0",
    "category": "Website",
    "license": "OPL-1",
    "author": "mytime.click",
    "website": "https://mytime.click",
    "depends": ["website"],
    "data": [
        "views/res_country_views.xml",
        "views/date_form_advanced_templates.xml",
        "views/gaesteregistrierung_templates.xml",
    ],
    "post_init_hook": "post_init_hook",
    "installable": True,
    "application": False,
}
