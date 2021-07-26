## User Experience

- ### User Stories

    As a **store owner**, I want to be able to:

    1. Add a product, so that I can add new items to my store.
    2. Edit a product, so thas I can change the details of the product such as its price, description, image and other properties. 
    3. Delete a product, so that I can remove items from my store that are no longer available.
    4. Add a blog post, so that I can add new content to my blog page to help drive traffic to my store.
    5. Edit a blog post, so thas I can change the details of the blog such as its title, content, image and other properties. 
    6. Delete a blog post, so that I can remove blog posts that are outdated or irrelevent.
    7. Delete a blog post comment, so that I can remove a comment that contains offensive content.
    8. Delete a product review, so that I can remove a review that contains offensive content.


- ### Wireframes

  The wireframes for this project were created using Balsamiq.

  - [Home Page](https://github.com/Johnny-Morgan/pickles/blob/master/docs/wireframes/home_page_wireframes.pdf)

  - [Products Page](https://github.com/Johnny-Morgan/pickles/blob/master/docs/wireframes/products_page_wireframes.pdf)

  - [Product Info Page](https://github.com/Johnny-Morgan/pickles/blob/master/docs/wireframes/products_info_page_wireframes.pdf)

  - [Basket Page](https://github.com/Johnny-Morgan/pickles/blob/master/docs/wireframes/basket_page_wireframes.pdf)

  - [Checkout Page](https://github.com/Johnny-Morgan/pickles/blob/master/docs/wireframes/checkout_page_wireframes.pdf)

  - [Blog Page](https://github.com/Johnny-Morgan/pickles/blob/master/docs/wireframes/blog_page_wireframes.pdf)

  - [Blog Post Page](https://github.com/Johnny-Morgan/pickles/blob/master/docs/wireframes/blog_post_page_wireframes.pdf)

- ### Design

  - #### Colour Scheme
    
    ![Image](https://github.com/Johnny-Morgan/pickles/blob/master/docs/readme_images/color_scheme.png)

    - Hookers Green #416A59
    - Asparagus #73A24E
    - Cadmium Orange #FB8B2E
    - Cornsilk #FFF7D3

    Two shades of green were chosen as the main colours of this website. Green was chosen because it is associated with nature, freshness and health. 
    
  - #### Typography

    [Inter](https://fonts.google.com/specimen/Inter) was chosen as the main font for this website with sans-serif as the fallback font.


## Information Architecture

SQLite was used in the development of this project as it is the default database used with Django. On deployment with Heroku, a Postgres database is used.

### Data Models

**Profiles App**

`User` model

Django's default [User](https://docs.djangoproject.com/en/3.2/ref/contrib/auth/) model is utilized for this project. 

`UserProfile` model 

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| User | user | OneToOneField 'User' | on_delete=models.CASCADE |
| Default Mobile Number | default_mobile_number | CharField | max_length=20, null=True, blank=True |
| Default Street Address 1 | default_street_address_1 | CharField | max_length=80, null=True, blank=True |
| Default Street Address 2 | default_street_address_2 | CharField | max_length=80, null=True, blank=True |
| Default Town or City | default_town_or_city | CharField | max_length=40, null=True, blank=True |
| Default County | default_county | CharField | max_length=40, null=True, blank=True |
| Default Postcode | default_postcode | CharField | max_length=20, null=True, blank=True |
| Default Country | default_country | CountryField | blank_label='Country', null=True, blank=True |

**Products App**

`Category` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Name | name | CharField | max_length=254 |
| Friendly Name | friendly_name | CharField | max_length=254, null=True, blank=True |

`Product` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Category | category | ForeignKey 'Category' | null=True, blank=True, on_delete=models.SET_NULL |
| SKU | sku | CharField | max_length=254, null=True, blank=True |
| Name | name | CharField | max_length=254 |
| Description | description | TextField |
| Price | price | DecimalField | max_digits=6, decimal_places=2 |
| On Sale | on_sale | BooleanField | default=False, null=True, blank=True |
| Image URL | image_url | URLField | max_length=1024, null=True, blank=True |
| Image | image | ImageField | null=True, blank=True |

`Review` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Product | product | ForeignKey 'Product' | related_name='reviews', on_delete=models.CASCADE |
| Name | name | CharField | max_length=100 |
| Email | email | EmailField |
| Review | review | TextField | max_length=500 |
| Rating | rating | CharField | max_length=1, null=True, choices=RATINGS, default='1' |
| Date | date | DateField | auto_now_add=True |

**Checkout App**

`Order` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Order Number | order_number | CharField | max_length=32, null=False, editable=False |
| User Profile | user_profile | ForeignKey 'UserProfile' | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' |
| First Name | first_name | CharField | max_length=50, null=False, blank=False |
| Last Name | lasst_name | CharField | max_length=50, null=False, blank=False |
| Email | email | EmailField | max_length=254, null=False, blank=False |
| Mobile Number | mobile_number | CharField | max_length=20, null=False, blank=False |
| Street Address 1 | street_address_1 | CharField | max_length=80, null=True, blank=True |
| Street Address 2 | street_address_2 | CharField | max_length=80, null=True, blank=True |
| Town or City | town_or_city | CharField | max_length=40, null=True, blank=True |
| County | county | CharField | max_length=40, null=True, blank=True |
| Postcode | postcode | CharField | max_length=80, null=True, blank=True |
| Country | country | CountryField | blank_label='Country *', null=True, blank=True |
| Date | date | DateTimeField | auto_now_add=True |
| Delivery Cost | delivery_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0 |
| Order Total | order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 |
| Grand Total | grand_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 |
| Original Basket | original_basket | TextField | null=False, blank=False, default='' |
| Stripe PID | stripe_pid | CharField | max_length=254, null=False, blank=False |

`OrderLineItem` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Order | order | ForeignKey 'Order' | null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' |
| Product | product | ForeignKey 'Product' | null=False, blank=False, on_delete=models.CASCADE |
| Quantity | quantity | IntegerField | null=False, blank=False, default=0 |
| Line Item Total | lineitem_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False |

![Image](https://github.com/Johnny-Morgan/pickles/blob/master/docs/readme_images/database_schema.png)

**Blog App**

`Tag` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Title | title | CharField | max_length=20 |

`Post` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Title | title | CharField | max_length=55 |
| Slug | slug | SlugField | unique=True, db_index=True |
| Intro | intro | TextField | max_length=254 |
| Date | date | DateTimeField | auto_now_add=True |
| Tags | tags | ManyToManyField 'Tag' | blank=True |
| Image URL | image_url | URLField | max_length=1024, blank=True, null=True |
| Image | image | ImageField | null=True, blank=True |
| Author | author | CharField | null=True, blank=True, max_length=254 |

`Comment` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Post | Post | ForeignKey 'Post' | related_name='comments', on_delete=models.CASCADE |
| Name | name | CharField | max_length=100 |
| Email | email | EmailField |
| Body | body | TextField | max_length=500 |
| Date | date | DateTimeField | auto_now_add=True |

![Image](https://github.com/Johnny-Morgan/pickles/blob/master/docs/readme_images/blog_schema.png)

## Testing

The testing data for this project can be found in a separate file called [TESTING.md](https://github.com/Johnny-Morgan/pickles/blob/master/TESTING.md).
