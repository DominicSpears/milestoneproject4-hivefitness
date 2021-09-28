### Contents

* Testing
  * [Solved bugs](#bugs)
  * [Remaining bugs](#remaining)
  * [Validator tests](#validator)
  * [Manual tests](#manual)
  * [User story tests](#user-story)

<a name="bugs"></a>

### Bugs Discovered
#### Solved Bugs

1. 
  * 

<a name="remaining"></a>

#### Remaining Bugs

1. 
  * 
<a name="validator"></a>

### Validator Tests

#### All html Pages
  * W3C HTML Validator - Document checking completed. No errors or warnings to show.

#### base.css
  * W3C CSS Validator - Congratulations! No Error Found.

#### stripe_elements.js
  * JSHint Code Tester - One warning 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).

#### All Python Pages
  * PEP8 Python Validator - All right

<a name="manual"></a>

### Manual Testing

1. Register
  * New users add a username and password to the input fields
  * Username and password(hashed) saved in the database, user lgged in to site
  * Result: pass



<a name="user-story"></a>

### User Story Tests

#### Site administrator
1. As a site administrator, I want the ability to edit and delete all recipes, even if I didn't write them myself.
  * To address this I added code that shows all recipes on the profile admin page, rather than just the recipes created by that user.
  * ![User Story 13](static/images/user-stories/userstory11.png)
