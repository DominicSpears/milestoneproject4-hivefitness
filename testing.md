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

#### Navbar

1. Logo home button
  * Click logo
  * User returned to home page
  * Result: pass

2. About button
  * Click about button
  * User taken to home page, about us section
  * Result: pass

3. Blog button
  * Click blog button
  * User taken to all posts page
  * Result: pass

4. Contact button
  * Click contact button
  * User taken to home page, contact us section
  * Result: pass

5. Shop button
  * Click shop button
  * Reveals dropdown menu with calssification options
  * Result: pass

5. Shop dropdown, all products button
  * Click All products category button
  * User taken to all products page
  * Result: pass

5. Shop dropdown, catgory button
  * Click any of the specific category buttons
  * User taken to products page, by category
  * Result: pass

5. Shop dropdown, sort button
  * Click any of the specific sort option buttons
  * User taken to products page, ordered by selected option
  * Result: pass

5. Search products bar
  * Type in selection
  * All relevant results show on products page
  * Result: pass

5. Profile button
  * Click profile button
  * Reveals dropdown menu
  * If not logged in, reveal register and login options only 
  * If logged in as user, reveal profile and logout options only
  * If logged in as super user, reveal management options 
  * Result: pass

5. Profile dropdown, register button
  * Click register button
  * User taken to register page
  * Result: pass

5. Profile dropdown, login button
  * Click login button
  * User taken to login page
  * Result: pass

5. Profile dropdown, profile button
  * Click my profile button
  * User taken to their personal profile page
  * Result: pass

5. Profile dropdown, logout button
  * Click logout button
  * User taken to logout page
  * Result: pass

5. Profile dropdown, manage product categories button
  * Click manage product categories button
  * Super user taken to manage product categories page
  * Result: pass

5. Profile dropdown, add product button
  * Click add product button
  * Super user taken to add product page
  * Result: pass

5. Profile dropdown, manage post categories button
  * Click my manage post categories button
  * Super user taken to manage post categories page
  * Result: 
  
5. Profile dropdown, add post button
  * Click add post button
  * Super user taken to add post page
  * Result: pass

5. Shopping bag button
  * Click shopping bag button
  * User taken to shopping bag page
  * Result: pass

#### Footer

1. Quick link buttons
  * Click each button
  * User taken to relevant page or part of homepage
  * Result: pass

1. Social media links
  * Click each link
  * Opens relevant social media page on new tab
  * Result: pass

#### Home Page

1. Feature card link buttons
  * Click each button
  * User taken to relevant page or part of homepage
  * Result: pass

1. Profile Feature card 
  * If logged in, message and link related to profile page
  * If logged out, message and link related to login page
  * Result: pass

1. Contact us form (valid message)
  * Fill in form with required info/message
  * Email sent to hivefitness92@gmail.com
  * Result: pass

1. Contact us form (invalid message)
  * Fill in form without required info/message
  * Tooltip reveals which section needs filling out
  * Result: pass

#### All Blogs Page

1. Categories buttons
  * Click each button
  * Reveal relevant blog articles
  * Result: pass

1. All posts buttons
  * Click all posts button
  * User taken to all posts page 
  * Result: pass

1. Blog management buttons
  * If logged in as super user, management buttons available
  * Result: pass

1. Blog edit button
  * Click edit button
  * Super user taken to edit post page
  * Result: pass

1. Blog delete button
  * Click delete button
  * Blog post deleted
  * Result: pass

1. Blog read more button
  * Click read more button
  * User taken to article page
  * Result: pass

#### Specific Blog Page

1. Blog management buttons
  * If logged in as super user, management buttons available
  * Result: pass

1. Blog edit button
  * Click edit button
  * Super user taken to edit post page
  * Result: pass

1. Blog delete button
  * Click delete button
  * Blog post deleted
  * Result: pass

1. Return button
  * Click return button
  * User taken to all posts page
  * Result: pass

1. Comments counter
  * Add/delete a comment
  * Comment counter goes up/down by 1
  * Result: pass

1. Comments form (valid message)
  * Fill in form with required info/message
  * Comment added to blog article
  * Result: pass

1. Contact us form (invalid message)
  * Fill in form without required info/message
  * Tooltip reveals which section needs filling out
  * Result: pass







<a name="user-story"></a>

### User Story Tests

#### Site administrator
1. As a site administrator, I want the ability to edit and delete all recipes, even if I didn't write them myself.
  * To address this I added code that shows all recipes on the profile admin page, rather than just the recipes created by that user.
  * ![User Story 13](static/images/user-stories/userstory11.png)
