# Issues before testing
1. The db did not initialize with schema.sql script, so every action in UI resulted in error. The breakpoint set at db.py:44 was not reached. Temporarily fixed by manually running script.sql on instance/demo_app.sqlite
2.

# Found problems
1. Even though the firstname/lastname/phone fields are mandatory in web page, they are not in the register() method in auth.py. Initially I used "submit form" at login page tests, and it did not simulate user behavior correctly and created users with partially complete data. Due to this behavior switched to button click 
