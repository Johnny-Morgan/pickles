# Testing

## Validation

### HTML

The [W3C Markup Validator](https://validator.w3.org/#validate_by_input) service was used to validate the HTML code of this project.

- [basket.html](https://github.com/Johnny-Morgan/pickles/blob/master/basket/templates/basket/basket.html) template errors:

    **Error:** *No p element in scope but a p end tag seen.*

    **Fix:** Change p element to a div element.

- [add_post.html](https://github.com/Johnny-Morgan/pickles/blob/master/blog/templates/blog/add_post.html) template errors:

    **Warning:** *The type attribute is unnecessary for JavaScript resources.*

    **Fix:** Remove type attribute from script.

- [edit_post.html](https://github.com/Johnny-Morgan/pickles/blob/master/blog/templates/blog/edit_post.html) template errors:

    **Error:** *Bad value for attribute action on element form: Must be non-empty.*

    **Fix:** Add ```"{% url 'edit_post' post.slug %}"``` to action attribute.

- [post.html](https://github.com/Johnny-Morgan/pickles/blob/master/blog/templates/blog/post.html) template errors:

    **Error:** *Bad value for attribute action on element form: Must be non-empty.*

    **Fix:** Add ```"{% url 'post' post.slug %}"``` to action attribute.

- [checkout.html](https://github.com/Johnny-Morgan/pickles/blob/master/checkout/templates/checkout/checkout.html) template errors:

    **Warning:** *Empty heading.* This warning is in relation to the h1 element containing the font awesome loading spinner and can be safely ignored.

- [carousel_item.html](https://github.com/Johnny-Morgan/pickles/blob/master/home/templates/home/carousel_item.html) template errors:

    **Error:** No p element in scope but a p end tag seen.

    **Fix:** Change p element to a div element.

- [home.html](https://github.com/Johnny-Morgan/pickles/blob/master/home/templates/home/home.html) template errors:

    **Warning:** *The type attribute is unnecessary for JavaScript resources.*

    **Fix:** Remove type attribute from script.

- [add_product.html](https://github.com/Johnny-Morgan/pickles/blob/master/products/templates/products/add_product.html) template errors:

    **Warning:** *The type attribute is unnecessary for JavaScript resources.*

    **Fix:** Remove type attribute from script.

- [product_info.html](https://github.com/Johnny-Morgan/pickles/blob/master/products/templates/products/product_info.html) template errors:

    **Error:** *No p element in scope but a p end tag seen.*

    **Fix:** Change p element to a div element.

    **Error:** *Duplicate attribute id.*

    **Fix:** Remove duplicate id. 

    **Error:** *The scope attribute on the td element is obsolete. Use the scope attribute on a th element instead.*

    **Fix:** Remove scope attributes from the td elements.

    **Error:** *Bad value for attribute action on element form: Must be non-empty.*

    **Fix:** Add ```"{% url 'product_info' product.id %}"``` to action attribute.

    **Warning:** *The type attribute is unnecessary for JavaScript resources.*

    **Fix:** Remove type attribute from script.

- [products.html](https://github.com/Johnny-Morgan/pickles/blob/master/products/templates/products/products.html) template errors:

   **Warning:** *The type attribute is unnecessary for JavaScript resources.*

    **Fix:** Remove type attribute from script.

- [base.html](https://github.com/Johnny-Morgan/pickles/blob/master/templates/base.html) template errors:

    **Error:** *Unclosed element div.*

    **Fix:** Add missing closing div tag.

    **Error:** *The aria-controls attribute must point to an element in the same document.*

    **Fix:** Change aria-controls attribute value from "main-nav" to "navigation"

### CSS

The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) service was used to validate the CSS code.

- base.css - no errors found.
- checkout.css - no errors found.
- profile.css - no errors found.

### Python

The Flake8 Python library was used for checking the code base against the PEP8 coding style and for checking for programming errors.

All the files passed with the following errors ignored:

- ```./blog/widgets.py:9:80: E501 line too long (83 > 79 characters)```

    ```python
    template_name = 'blog/custom_widget_templates/custom_clearable_file_input.html'
    ```

    Fixing this line would break the variable so I chose to ignore this error.

- ```./products/test_forms.py:60:80: E501 line too long (92 > 79 characters)```

    ```python
    self.assertEqual(
                form.errors['price'][0],
                'Ensure that there are no more than 4 digits before the decimal point.')
    ```

    This line is testing the form error message, breaking this line up would cause the test to fail, therefore it is ignored.

- ```./products/widgets.py:9:80: E501 line too long (87 > 79 characters)```

    ```python
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
    ```

    Fixing this line would break the variable so I chose to ignore this error.

- ```./checkout/apps.py:9:9: F401 'checkout.signals' imported but unused```

    Safely ignored.

- ```./checkout/webhook_handler.py:70:80: E501 line too long (80 > 79 characters)```

    ```python
    profile.default_street_address1 = shipping_details.address.line1
    ```

    This could be fixed by assigning shipping_details.address.line1 to a variable first:

    ```python
    details = shipping_details.address.line1
    profile.default_street_address1 = details
    ```

    However this solution would inhibit code readability and is therefore ignored.

- ```./checkout/webhook_handler.py:71:80: E501 line too long (80 > 79 characters)```

    As above.

- All errors in auto-generated lines in settings.py are ignored.

- All errors in the auto-generated migrations files are ignored.

- All Rule DJ01 - 'Avoid using null=True on string-based fields such as CharField and TextField' are ignored.

## Testing User Stories

- As a **store owner**, I want to be able to:

    1. *Add a product, so that I can add new items to my store.*

        Store owners have access to a Product Admin page which contains a form that allows them to a add a new product to the store. 
        
        ![Add a Product Gif](docs/testing_gifs/add_product.gif)


    2. *Edit a product, so thas I can change the details of the product such as its price, description, image and other properties.*

        On the product info page for each product, an edit product button is displayed for store owners. Clicking this button directs the store owner to a form where they can edit the details of the product.

        ![Edit a Product Gif](docs/testing_gifs/edit_product.gif)


    3. *Delete a product, so that I can remove items from my store that are no longer available.*

        On the product info page for each product, a delete product button is displayed for store owners. Clicking this button opens a modal which askes the user if they wish to delete the product. Clicking the modal delete button removes the item from the store.

        ![Delete a Product Gif](docs/testing_gifs/delete_product.gif)


    4. *Add a blog post, so that I can add new content to my blog page to help drive traffic to my store.*

        On the blog page, an Add Blog Post button is displayed for store owners. Clicking the button directs the user to a new page where a form is displayed for adding a new blog post.

        ![Add a Blog Post Gif](docs/testing_gifs/add_blog_post.gif)


    5. *Edit a blog post, so thas I can change the details of the blog such as its title, content, image and other properties.*

        In each blog post page, there is a button located below the blog post content, visible only to store owners. Clicking the button directs the user to a form where the blog post details can be edited.

        ![Add a Blog Post Gif](docs/testing_gifs/edit_blog_post.gif)


    6. *Delete a blog post, so that I can remove blog posts that are outdated or irrelevent.*

        In each blog post page, there is a button located below the blog post content, visible only to store owners. Clicking this button opens a modal which askes the user if they wish to delete the blog post. Clicking the modal delete button removes the blog post.

        ![Add a Blog Post Gif](docs/testing_gifs/delete_blog_post.gif)


    7. *Delete a blog post comment, so that I can remove a comment that contains offensive content.*

        There is a delete button under every blog post comment that is visible to only store owners. Clicking this button opens a modal which askes the user if they wish to delete the comment. Clicking the modal delete button deletes the comment.

        ![Add a Blog Post Gif](docs/testing_gifs/delete_comment.gif)
    

    8. *Delete a product review, so that I can remove a review that contains offensive content.*

        There is a delete button under every review that is visible to only store owners. Clicking this button opens a modal which askes the user if they wish to delete the review. Clicking the modal delete button deletes the review.

        ![Add a Blog Post Gif](docs/testing_gifs/delete_review.gif)



    As a **visitor**, I want to be able to:

    1. Easily register for an account so that I can login and view my account.
        
        A register link located in the navbar directs the visitor to a register page where they can input their account details. On completion of the signup form, an email is sent to the user asking them to confirm their email address. Once they connect their email to their account thay can login to the site.

        ![Register New account Gif](docs/testing_gifs/register_new_account.gif)

    2. View all the available products so I can choose some to purchase.

        In the navbar there is a menu option called 'All Products' which when clicked, redirects the user to a page containing all the products in the shop.

        ![All Products Gif](docs/testing_gifs/all_products.gif)

    3. Sort the all of the available products based on their price, name or category.

        Shoppers have the option to sort products by their price or category by clicking on the relevent links in the navbar. There is also a sort selector box where a user can sort by products by price, name and category.

        ![Sorting Products Gif](docs/testing_gifs/sorting_products.gif)

     4. View a particular category of products so I can find products I am interested in faster.

        In the navbar, users can click on the 'PLANTS' or 'SEEDS' option which opens a submenu giving the user additional options on the type of plants or seeds they wish to view.

    5. Sort a particular category of products based on their price, name or category.

        When a user chooses an option from a submenu for example 'Fruit Trees' the products displayed are filtered to only show fruit trees. By clicking on the 'Sort by...' button, users can sort the fruit trees by price or name.

        ![Sorting Fruit Trees Gif](docs/testing_gifs/sorting_fruit_trees.gif)

    6. Sort multiple categories of products simultaneously to find the best priced products across broad categories such as plants or seeds.

        Clicking on the 'All Plants' submenu option will display all of the fruit trees, fruit bushes and vegetable plants. Clicking on the 'All Seeds' option will display all of the vegetable seeds and bulbs.
    
    7. View the details of an individual product such as its price, description and reviews.

        By clicking on a products image, or by clicking on the information button, users are redirected to the products information page where they can view more details on the product.

        ![Product Info Gif](docs/testing_gifs/product_info.gif)

    8. Leave a review of a product so I can let other shoppers know what I think of the product.

        On each individual product's information page there is a 'Leave a Review' button which opens a form for a user to leave a review for that particular product.

        ![Image](docs/testing_images/review_form.png)

    9. Search for a product by name or description so that I can quickly find a specific product.

        A search bar is located in the navbar which can be used to search products based on their name and description. 

        ![Product Search Gif](docs/testing_gifs/product_search.gif)

    10. Quickly see search results and the number of results.

        The number of products found and the original search term are displayed above the search results. 

        ![Image](docs/testing_images/search_results.png)

    11. Quickly add a product to my basket without having to view that product's individual page.

        Clicking on the shopping basket icon will add a product to the shopping basket. A toast will be displayed confirming the successful adding of the product.

        ![Quick Add To Basket Gif](docs/testing_gifs/quick_add.gif)

    12. Easily select the quantity of a product when purchasing it.

        A select element is provided where a shopper can easily select the quantity of a product they wish to purchase.

        ![Select Quantity Gif](docs/testing_gifs/select_quantity.gif)

    13. View the products in my shopping basket to be purchased.

        Clicking on the shopping basket icon in the navbar will redirect the user to a shopping baket page. This page displays the contents of the user's shopping basket. When a user adds an item to their shopping basket, a toast is displayed which gives them the option of viewing their basket.

        ![View Basket Gif](docs/testing_gifs/view_basket.gif)

    14. Adjust the quantity of individual items in my shopping basket.

        Each product in the shopping basket contains a select element which a user can use to adjust the quantity of the product in the basket. Clicking 'update' wil update the quantity and clicking the red 'x' will delete the product from the basket.

        ![View Basket Gif](docs/testing_gifs/view_basket.gif)

    15. Easily view the total value of my purchases at any time.

        The shopping basket icon in the navbar shows the current value of the shopping basket. It is visible on all devices and on every page of the website. 

        ![Image](docs/testing_images/basket.png)

    16. Quickly enter my personal and payment information so that I can check out fast and hassle free.

        Clicking on the checkout button will redirect the user to the checkout page. A form is provided for the user to input their details and make a payment. If the user has saved their delivery details previously, the form will be prepopulated with these details.

    17. View an order confirmation and receive an email confirmation after completing a purchase.

        On completing the checkout process, a toast is displayed which confirms the order has been received, displays the order number and tells the user a confirmation email has been sent. An order summary is also displayed showing all of the order information. 

        ![Complete Order Gif](docs/testing_gifs/complete_order.gif)

    18. Leave a comment on a blog post so I can contribute to a subject I am interested in.

        Under each blog post there is a form where a user can add a comment relating to the blog post. 

        ![Complete Order Gif](docs/testing_gifs/add_comment.gif)


    As a **registered user**, I want to be able to:

    1. Easily login or logout of my account.

        A login link located in the navbar directs the user to the login page where the user can login with their usernam or email address. Once logged in the navbar provides a link to logout. Clicking this link directs the user to a logout page where they are asked to confirm they want to sign out.

        ![Register New account Gif](docs/testing_gifs/sign_in_sign_out.gif)

    2. Easily recover my password if I forget it.

        A 'Forgot Password?' link is provided below the sign in button. Clicking the link redirects the user to a password reset page.

        ![Forgot Password Gif](docs/testing_gifs/forgot_password.gif)

    3. Have a personalized user profile page so that I can view my order history and delivery information.

        Each registered user has a profile page which contains a list of their previous orders and a form where the user can update their delivery information.
        
        ![Image](docs/testing_images/profile.png)
        
    4. Easily add or update my delivery information.

        A user's delivery information can be easily updated using the form provided on their profile page.

## Manual Testing on Live Site

### Navigation

- Click the logo in the navbar, confirm that it directs to the home page.
- Click the 'ALL PRODUCTS' link, confirm it displays the correct sections in the dropdown menu.
- Click the 'PLANTS' link, confirm it displays the correct sections in the dropdown menu.
- Click the 'SEEDS' link, confirm it displays the correct sections in the dropdown menu.
- Click each link in each dropdown menu, confirm each display the correct products.
- Click the 'BLOG' link, confirm it directs to the blog page.
- Click the 'Account' link as a non logged-in user, confirm it displays a submenu with 'Register' and 'Login'.
- Log in as a non-superuser, confirm that the 'Account' dropmenu displays 'My Profile' and 'Logout'.
- Log in as a superuser, confirm that the 'Account' dropmenu displays 'Product Admin', 'My Profile' and 'Logout'.
- Click each link in the 'Account' submenus, confirm each directs to the correct page.
- Add an item to the users basket, confirm that the basket total changes to correct value.
- Delete all items in the shopping basket, confirm that the basket total changes to €0.00.
- Search for a product in the search bar, confirm that the results of the search are displayed correctly.
- Change the discount percentage variable in settings.py, confirm the discount percentage value updates in the site banner.

### Footer

- Click on all social media links, confirm they open the correct page in a new browser tab.

### Home Page

- Observe the carousel displaying the latest offers, confirm it updates as expected.
- Click on the carousel arrows, confirm the carousel changes as expected.
- Click on the image for each product, confirm it directs to the correct page.
- Click on the information icon for each product, confirm it directs to the correct page.
- Click on the shopping basket icon for each product, confirm it adds one item of the product to the shopping basket.

### Products Page

- Click on the image for each product, confirm it directs to the correct page.
- Click on the information icon for each product, confirm it directs to the correct page.
- Click on the shopping basket icon for each product, confirm it adds one item of the product to the shopping basket.
- Hover over each product card, confirm the shadow effect takes place.
- Click each option in the 'Sort by...' select box, confirm each sort result displays the correct products.
- Click the category for each product, confirm each product for that category is displayed.
- Change the discount percentage variable in settings.py, confirm the price for discounted products updates and displays the correct value.

### Individual Product Page

- Click on the product image, confirm it opens the image in a new tab.
- Click on the product category, confirm it returns to the product page containing all products with that category.
- Confirm that the edit and delete buttons are visible to logged in superusers.
- Confirm that the quantity input updates when a new quantity is selected.
- Click the 'ADD TO BASKET' button, confirm the basket updates with the desired quantity.
- Click the 'BACK TO SHOP' button, confirm it redirects to the products page showing all products.
- Click the accordion elements, confirm they open and close in the correct manner.
- Confirm that the product rating score is correct based on the exisitng product reviews.
- Confirm 'No reviews yet!' is dispayed for a product that has no reviews.
- Click on the 'Leave a Review' button, confirm it displays a form to write a product review.
- Attempt to submit the review form with invalid data, confirm the relevent warning messages are displayed.
- Fill out the review form correctly and submit, confirm the review is displayed first in the list of reviews.
- Confirm that the product rating score updates based on the rating given in the submitted review.
- Confirm the pagination links are working correctly for products with more than 5 reviews.

### Shopping Basket Page

- Attempt to access the basket page with an empty basket, confirm the message 'Your shopping basket is empty.' is shown and a button directing the shopper back to the shop is provided.
- Click the 'BACK TO SHOP' button and confirm it takes the user to the products page.
- Add products to the basket and return to the basket page, confirm all the products and quantities displayed in the basket are correct and the subtotal, basket total and order total are correct.
- Adjust the quantity field of a product and click the update button, confirm that the quantity and subtotal is updated as well as the basket subtotal and order total.
- Click the 'x' delete button for a product in the basket, confirm that the product is deleted from the basket and the basket and order totals are updated.
- Confirm that a basket total that is less than €60 has a delivery charge of €6.99.
- Confirm that a basket total that is more than €60 has no delivery charge.
- Click the 'CHECKOUT' button and confirm it takes the user to the checkout page.

### Checkout Page

- Attempt to access the checkout page with an empty basket, confirm user is redirected to the products page and an error message is displayed
- Confirm that the products in order summary match the products in the basket.
- Confirm that the basket total, delivery charge and order total are correct.
- Confirm that the text 'Create an account or login to save this information' is displayed under the delivery details section of the form for a non logged in visitor.
- Check that clicking the 'Create an account' link redirects the visitor to the signup page.
- Check that clicking the 'login' link redirects the visitor to the login page.
- Confirm that the text 'Save this delivery information to my profile' with a checked box is displayed under the delivery details section of the form for a logged in user.
- Confirm that the order form is prepopulated with the delivery information of the user if that user has saved their information previously.
- Click the 'Adjust basket' button, confirm it redirects the user to the shopping basket page.
- Attempt to submit the form with incorrect data, confirm the relevent warning messages are displayed.
- Submit the form with correct data, confirm that the loading overlay is displayed and an order summary is displayed after the loading overlay finishes. Confirm that a toast message is displayed with a confirmation that the order has been received, confirm that it shows the order number and that an email will be sent to the user.
- Confirm that a confirmation email is sent to the user.

### Blog Page

- Confirm the 'Add Blog Post' button is only visible to logged in superusers.
- Click the 'Add Blog Post' button to confirm the user is directed to add blog post page which contains a form for adding a new blog post.
- Attempt to submit the form with incorrect data, confirm the relevent warning messages are displayed.
- Attempt to add a new blog post with the title of an already existing blog post, confirm a toast message appears with an error warning and a message prompting the user to enter a different title.
- Fill out the form with correct data, confirm the user is directed back to the blog page and the new blog post appears at the top of the list of blog posts.
- Confirm that adding a blog post without an image will result in the no-image-icon.png image from the media directory will be used as the blog post image.
- Click on each blog post image, confirm it directs to the correct blog post page.
- Click on each '...read more' text at the end of each blog intro, confirm it directs to the correct blog post page.
- Confirm the pagination links are working correctly.

### Blog Post Page

- Confirm that the edit and delete buttons are visible to logged in superusers.
- Click the edit button, confirm the user is directed to the 'edit post' page.
- Confirm the correct the form to edit the blog post is populated with the blog post data.
- Attempt to submit the form with incorrect data, confirm the relevent warning messages are displayed.
- Attempt to edit the title to the title of an already existing blog post, confirm a toast message appears with an error warning and a message prompting the user to enter a different title.
- Submit the form with correct data, confirm the blog post updates with the new data.
- Click the 'Back' button, confirm it redirects to the blog page.
- Click the delete button, confirm a modal appears with a message asking the user are they sure they want to delete the post.
- Confirm that clicking the modal cancel button returns the user to the blog post page without deleting it.
- Click the modal delete button, confirm that the blog post is deleted.
- Confirm 'No comments yet!' is displayed for a blog post that has no comments.
- Attempt to fill out the 'Leave a comment' form with invalid data, confirm the relevent warning messages are displayed.
- Submit the form with valid data, confirm the comment appears at the top of the list of comments.
- Confirm that a button for deleting comments is visible only to superusers.
- Hover over the delete comment button, confirm that the 'Delete Comment' tooltip appears to the right of the button.
- Click the delete comment button, confirm a modal appears with a message asking the user are they sure they want to delete the comment.
- Confirm that clicking the modal cancel button returns the user to the blog post page without deleting the comment.
- Click the modal delete button, confirm that the comment is deleted.

## Bugs

### Solved Bugs

- If a superuser attempted to create a new blog post with a title that matched the title of an existing blog post, an IntegrityError would occur. This Unique constraint failure was occuring because the slug for each blog post must be unique. 

    ![Image](docs/testing_images/blog_slug_bug.png)

    **Fix:** To fix this a list of the existing slugs is created in the view.

    ```python
    slugs = list(Post.objects.all().values_list('slug', flat=True))
    ```
    In the POST request before the blog post object is saved to the database, there is a check to determine if the slug is contained in the list of existing slugs. If it is in the list, a message is displayed prompting the user to enter a different title. Otherwise the post is saved successfully to the database.

    ```python
    if post.slug in slugs:
        messages.error(request, 'A blog post with that title \
            already exists, please enter a different title.')  
    else:
        post.save()
        messages.success(request, f'Blog post "{post.title}" \
                        successfully added!')
        return redirect('blog')
    ```

    ![Image](docs/testing_images/blog_slug_error_message.png)

- The above error also occured if a superuser was editing a blog post and changed the title to that of an existing blog post title. The same fix was used as above but this introduced a new bug. Now when editing a post, even if the title of the post was not edited, the error message would be displayed. This occured because the list of existing slugs in the database already contained the slug for the post that was being edited. Therefore the check to see if the list contained the slug always returned True, which in turn always displayed the error message. 

    **Fix:** In the edit_post view, remove the slug for the post that is being edited from the list of existing slugs.

    ```python
    slugs.remove(post.slug)
    ```

- If a superuser edited a blog post that was created by a different superuser, the author field would be updated to the superuser who edited the post. This occured because author field for a blog post was being updated in the edit_post view.

    ```python
    post.author = str(request.user)
    ```
    
    **Fix:** Remove the above line of code from the edit_post view. In future development the author field for a blog post can be related to the Django User model.

- When adding a new blog post, the tags field was not saving to the database. The post model's tags field is a ManyToManyField that points at the Tag model. To save the tags field form data, the save_m2m method can be used. 

    **Fix:** Invoke the save_m2m() method to save the many-to-many form data. Apply it when editing a blog post too.
    
    ```python 
    form.save_m2m()
    ```