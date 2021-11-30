# odoo-tools

## print_fields_for_view.py
findes all fields in python file and prints them in a suitable format for views. You can then copy-paste them easily.
```bash
python3 print_fields_for_view.py ./models/dummy.py
```

## manage_security_files.py
Complete security files management, you don't need to edit any `ir.access.module.csv` ever.
Menus are quite self explanetory, commandline usage:
```
manage_security_files.py [-d|-v] [path/to/module]
```

`-d` debug autput
`-v` verbose

If you don't give the module name it will ask for it.
