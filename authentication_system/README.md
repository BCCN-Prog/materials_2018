# Create a simple authentication system

### Basic API:
  - a function `get_credentials` that asks for username and password
  - a function `authenticate` that checks if user is the password database and that the password is correct
  - a function `add_user` to add a new user with password to the database
  - a function `read_pwdb` to read the password database from disk
  - a function `write_pwdb` to write the password database to disk

### Expected usage:
  - run the script
  - the script asks for username and password
  - if the user is known and password is correct: print the password database
  - if the user is not known, ask to add it to the password database
  - if a user has been added, store the updated database to disk

### Later, think about the following problems:
  - should we return different errors is username is not known or password is wrong? ⟶ do not leak valid usernames
  - password hashing ⟶ do not store passwords in clear text (database could be stolen, admins are nosy), do not store the password at all but only its hash (database could be stolen)
  - salting ⟶ different users with same passwords should not have same hash ⟶ cracking one does not crack all: mitigates dictionary attacks)

### Try to crack it! (Advanced)
  - can you guess the *hash collision* risk for the proposed solution?
  - try first a *brute force* attack
  - try a dictionary attach (you can use this list of [probable passwords](https://github.com/danielmiessler/SecLists/tree/master/Passwords)

### Notes 
To make it for real:
  - insecure temporary file (temp race attack) ⟶ [`tempfile`](https://docs.python.org/3/library/tempfile.html) and its context managers
  - better way of generating passwords or random tokens: module [`secrets`](https://docs.python.org/3/library/secrets.html)
  - cracking a password database is a form of art, see [John the Ripper password cracker](http://www.openwall.com/john/)
