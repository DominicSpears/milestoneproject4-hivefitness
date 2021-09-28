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


<a name="remaining"></a>

#### Remaining Bugs

1. Blog article text
  * Blog article does not include new paragraphs. 

2. Homepage links
  * Homepage links (about / contact us) create a blank blobk above the section when clicked.


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
  * Result: 
  
#### Blog Category management Page

1. Add post button
  * Click add post button
  * Super user taken to add post page
  * Result: pass

1. Blog category edit button
  * Click edit button
  * Super user taken to edit post page
  * Result: pass

1. Blog category delete button
  * Click delete button
  * Blog category deleted
  * Result: pass

#### Blog Category Add Page

1. Category Form
  * Submit valid form with category info
  * Category added to database
  * Result: pass

2. Cancel button
  * Click cancel button
  * Returns user to blog management page
  * Result: pass 

2. Add product category button
  * Click add post category button
  * Submits form and adds category to database
  * Result: pass 

#### Blog Category edit Page

1. Category Form
  * Form auto fils with category info
  * Result: pass

2. Cancel button
  * Click cancel button
  * Returns user to blog management page
  * Result: pass 

2. Update post category button
  * Click update product category button
  * Submits form and updates info
  * Result: pass 

#### Shop Page

1. Sort by dropdown
  * Select option in the dropdown menu
  * Products sorted by selected option
  * Result: pass

1. Product counter
  * Number of products depending on category selected
  * Result: pass

1. Product management buttons
  * If logged in as super user, management buttons available
  * Result: pass

1. Product edit button
  * Click edit button
  * Super user taken to edit product page
  * Result: pass

1. Product delete button
  * Click delete button
  * Product deleted
  * Result: pass

1. Back to top button
  * Click back to top button
  * Return user to top of the page
  * Result: pass

#### Product detail Page

1. Product management buttons
  * If logged in as super user, management buttons available
  * Result: pass

1. Product edit button
  * Click edit button
  * Super user taken to edit product page
  * Result: pass

1. Product delete button
  * Click delete button
  * Product deleted
  * Result: pass

1. Quantity selector
  * Click add/minus button
  * Adds/minus number of products to be added to bag
  * Result: pass

1. Keep shopping button
  * Click keep shopping
  * Returns user to all products page
  * Result: pass

1. Add to bag button
  * Click add to bag
  * Adds selected product/s to bag
  * Success message appears with order summary and checkout button
  * Result: pass

#### Shopping bag

1. Quantity plus/minus
  * Click plus/minus then update
  * Increases/decreases number of products
  * Result: pass

1. Remove button
  * Click remove button
  * Remove product from shopping bag
  * Result: pass

1. Keep shopping button
  * Click keep shopping
  * Returns user to all products page
  * Result: pass

1. Secure checkout button
  * Click secure checkout
  * User taken to checkout
  * Result: pass

#### Checkout 

1. Checkout form
  * Saved details appear automatically
  * Result: pass

1. Order summary  
  * Lists all products added to bag
  * Result: pass

1. Adjust bag button
  * Click adjust bag button
  * User returned to shopping bag
  * Result: pass

1. Complete order button
  * Click complete order
  * Order finalised, confirmation email sent to customer email
  * Result: pass

#### Product Category Management Page

1. Add product button
  * Click add product button
  * Super user taken to add product page
  * Result: pass

1. Product category edit button
  * Click edit button
  * Super user taken to edit product page
  * Result: pass

1. Product category delete button
  * Click delete button
  * Product deleted
  * Result: pass

#### Product Category Add Page

1. Category Form
  * Submit valid form with category info
  * Category added to database
  * Result: pass

2. Cancel button
  * Click cancel button
  * Returns user to blog management page
  * Result: pass 

2. Add product category button
  * Click add product category button
  * Submits form and adds category to database
  * Result: pass 

#### Product Category Edit Page

1. Category Form
  * Form auto fils with category info
  * Result: pass

2. Cancel button
  * Click cancel button
  * Returns user to blog management page
  * Result: pass 

2. Update product category button
  * Click update product category button
  * Submits form and updates info
  * Result: pass 

#### Profile Page

1. Profile form
  * Contains current user info if saved
  * Result: pass

1. Update profile form button
  * Fill in for with required info and click update
  * New info saved to database
  * Result: pass

1. Order history
  * Complete valid order
  * Shows last order as well as all previous order information
  * Result: pass


<a name="user-story"></a>

### User Story Tests

#### Casual Visitor

|As a/an           |I want to be able to                         |So that I can                                           |
|------------------|---------------------------------------------|--------------------------------------------------------|
|Casual Visitor    |Read information about the site              |Know what the site offers                               |
|Casual Visitor    |Easily navigate the site                     |Access any specific tool or product                     |
|Casual Visitor    |Regiter with the site                        |Become a user                                           |
|Casual Visitor    |See all blog articles                        |Access the information provided                         |
|Casual Visitor    |Contact the site administrators              |Report a problem/ request information                   |

To address these stories:
* I created an about us page that gives a bit of background about the site and what it has to offer.
* I created a navigation menu that is fixed to the top of all pages.
* I created a navigation menu that is fixed to the top of all pages.
* I created all posts page, accessable to anyone, that shows a list of all current articles.
* I created a contact us section of the hompage that links directly to the sites email address.
  * ![User Story 13](static/images/user-stories/userstory11.png)

|As a/an           |I want to be able to                         |So that I can                                           |
|------------------|---------------------------------------------|--------------------------------------------------------|
|Shopper           |Access the shop from any page of the site    |Get to the shop easily                                  |
|Shopper           |See a display of all products                |Scan through the site's full collection                 |
|Shopper           |Click on a product                           |See extra information an a rating                       |
|Shopper           |Search for products                          |Look for specific items                                 |
|Shopper           |Narrow down the products by category         |See all items in a specfic genre                        |
|Shopper           |Order the products by price/category/etc     |Easily search through a long list of items              |
|Shopper           |Review my order in a checkout                |Check that my order is correct before confirmation      |

To address these stories:
* I created a fixed navigation menu that allows access to the shop link from any page.
* I created an all products page that lists all current products on offer in the store.
* I created a product detail page so that each product could be expaned and see all relevant information.
* I created a searchbar that can filter through the list of current products to any relevant results.
* I created a series of categories, with links to each category, to narrow down a customer search.
* I created a selection of options for the customers to sort the orderr of products including price, name, category and rating.
* I created a shopping bag and a checkout app, each of which allows the shopper to review their order.

|As a/an           |I want to be able to                         |So that I can                                           |
|------------------|---------------------------------------------|--------------------------------------------------------|
|Registered User   |Save personal information                    |Enter it once only                                      |
|Registered User   |See a profile page                           |Add or update my personal information                   |
|Registered User   |See a list of previous orders                |Confirm what I have already purchased and when          |
|Registered User   |Register my own login information            |Log into the site securely                              |
|Registered User   |Get to associated social media sites         |Get further information/content                         |
|Registered User   |Leave comments on any blog post              |Be part of the community discussion                     |

To address these stories:
* I created a profile page in which users can save their information. (As well as at the checkout)
* I created a personal profile page with an information form that can be updated.
* I created an order history that is included on the profile page.
* I created a secure register and login page so that users can create an individual profile.
* I created social media links, located in the footer, that open the site website on a new tab.
* I added a comment system to the blog articles so that users can leave their opinions known. 

|As a/an           |I want to be able to                         |So that I can                                           |
|------------------|---------------------------------------------|--------------------------------------------------------|
|Site administrator|Add, edit or delete products as required     |Maintain the online shop                                |
|Site administrator|Manage the product categories                |Ensure the products can be easily searched/narrowed down|
|Site administrator|Add, edit or delete post articles as required|Maintain the blog posts                                 |
|Site administrator|Manage the post categories                   |Ensure the posts can be easily searched/narrowed down   |
|Site administrator|See the number of comments on each post      |Indicate which posts are getting the most traffic       |
|Site administrator|Edit or delete a blog comment                |Update mistakes or remove inappropriate content         |

To address these stories:
* I created product management buttons on the all products page and product detail page, to edit and delete products. As well as an indipended page to add products. 
* I created a product category management page, where ategories can be added, edited or deleted as needed.
* I created post management buttons on the all post page and post detail page, to edit and delete posts. As well as an indipended page to add posts.
* I created a post category management page, where post categories can be added, edited or deleted as needed.
* I created a comment counter that appear uner each article, so that the number of comments left is clear.
* I created comment management buttons to edit or delete comments, for super users only.