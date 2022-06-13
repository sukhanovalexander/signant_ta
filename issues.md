# Issues before testing
1. The db did not initialize with schema.sql script, so every action in UI resulted in error. The breakpoint set at db.py:44 was not reached. Temporarily fixed by manually running script.sql on instance/demo_app.sqlite.
2. 

# Found problems
1. Even though the firstname/lastname/phone fields are mandatory in web page, they are not in the register() method in auth.py. Initially I used "submit form" at login page tests, and it did not simulate user behavior correctly and created users with partially complete data. Due to this behavior switched to button click 
2. Github page states that GET request on route /api/users requires token. However, any user can access data even including not valid token. Corresponding method does not have @tokeqrequired decorator
3. Any user with valid token can access another user details on route /api/users/{username}
4. Any user with valid token can change other users details using put method
5. It is possible to create new user with empty password or empty username and password simultaneously using POST method
6. PUT request does not change password. After sending new password I can still issue token with old password
7. 