{
    "name": "hspl_test_prachi_brahmbhtt",
    "description": "A simple Test-model application",
    "summary": "A sheet for membership_level",
    "version": "0.1.0",
    "category": "Productivity",
    "sequence": -1,
    "author": "prachi_brahmbhatt",
    "depends": [
        "base","sale"

    ],
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "data/membership_level_demo.xml",
        "views/membership_level.xml",
        "wizard/wizardtest.xml",
        "views/inherit.xml",
       ],
    "installable": True,
    "application": True,
    "license": "LGPL-3"

}