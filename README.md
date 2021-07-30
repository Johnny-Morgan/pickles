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

    As a **visitor**, I want to be able to:

    1. Easily register for an account so that I can login and view my account.
    2. View all the available products so I can choose some to purchase.
    3. Sort the all of the available products based on their price, name or category.
    4. View a particular category of products so I can find products I am interested in faster.
    5. Sort a particular category of products based on their price, name or category.
    6. Sort multiple categories of products simultaneously to find the best priced products across broad categories such as plants or seeds.
    7. View the details of an individual product such as its price, description and reviews.
    8. Leave a review of a product so I can let other shoppers know what I think of the product.
    9. Search for a product by name or description so that I can quickly find a specific product.
    10. Quickly see search results and the number of results.
    11. Quickly add a product to my basket without having to view that product's individual page.
    12. Easily select the quantity of a product when purchasing it.
    13. View the products in my shopping basket to be purchased.
    14. Adjust the quantity of individual items in my shopping basket.
    15. Easily view the total value of my purchases at any time.
    16. Quickly enter my personal and payment information so that I can check out fast and hassle free.
    17. View an order confirmation and receive an email confirmation after completing a purchase.
    18. Leave a comment on a blog post so I can contribute to a subject I am interested in.

    As a **registered user**, I want to be able to:

    1. Easily login or logout of my account.
    2. Easily recover my password if I forget it.
    3. Have a personalized user profile page so that I can view my order history and delivery information.
    4. Easily add or update my delivery information.

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

## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

- [Python](https://www.python.org/)

- [JavaScript](https://www.javascript.com/)


### Frameworks, Libraries & Programs Used

- [Django](https://www.djangoproject.com/) - Django is a Python-based free and open-source web framework.

- [jQuery](https://jquery.com/) - jQuery is used to simplify the JavaScript code and DOM manipulation.

- [Bootstrap 4.4](https://getbootstrap.com/) - Bootstrap is used to assist with the responsiveness and styling of the website.

- [Heroku](https://www.heroku.com/home) - Heroku is used to deploy this website.

- [AWS](https://aws.amazon.com/?nc2=h_lg) - AWS Simple Cloud Storage S3 is used for storing static and media files.

- [Stripe](https://stripe.com/en-gb-de) - Online payment processing and credit card processing platform for this site.

- [SQLite](https://www.sqlite.org/index.html) - SQLite was used in the development of this project as it is the default database used with Django. 

- [PostgreSQL](https://www.postgresql.org/) - On deployment with Heroku, a Postgres database is used.

- [GitPod](https://gitpod.io) - GitPod was used as the IDE for this project.

- [Git](https://git-scm.com/) - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

- [GitHub](https://github.com/) - GitHub is used to store the project's code after being pushed from Git.

- [Balsamiq](https://balsamiq.com/) - Balsamiq was used to create the wireframes during the design process.

- [Google Fonts](https://fonts.google.com/specimen/Inter?query=inter) - Google Fonts was used to obtain the Inter font.

- [Font Awesome](https://fontawesome.com/) - Font Awesome is used to obtain the icons used in this website.

- [Autoprefixer](https://autoprefixer.github.io/) - Autoprefixer was used to add vendor prefixes.

- [Favicon.io](https://favicon.io/favicon-generator/) - was used to generate the favicons.

### Dependencies

- [asgiref](https://pypi.org/project/asgiref/) - ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and positioned as an asynchronous successor to WSGI.

- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - Used to create, configure, and manage AWS S3.

- [botocore](https://botocore.amazonaws.com/v1/documentation/api/latest/index.html) - Botocore provides the low level clients, session, and credential & configuration data.

- [coverage](https://coverage.readthedocs.io/en/coverage-5.5/) - Used to gauge the effectiveness of tests. It shows which parts of the code are being exercised by tests, and which are not.

- [dj-database-url](https://pypi.org/project/dj-database-url/) - A utility to help you load your database into your dictionary from the DATABASE_URL environment variable. Heroku uses environment variables for your database and other addons.

- [Django](https://www.djangoproject.com/) - Django is a Python-based free and open-source web framework.

- [django-allauth](https://django-allauth.readthedocs.io/en/latest/) - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.

- [django-countries](https://pypi.org/project/django-countries/) - A Django application that provides country choices for use with forms, flag icons static files, and a country field for models.

- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Provides a |crispy filter and {% crispy %} tag that lets you control the rendering behavior of Django forms in a very elegant and DRY way.

- [django-storages](https://pypi.org/project/django-storages/) - Provides a variety of storage backends in a single library.

- [gunicorn](https://docs.gunicorn.org/en/stable/) - The Gunicorn "Green Unicorn" is a Python Web Server Gateway Interface HTTP server.

- [jmespath](https://pypi.org/project/jmespath/) - JMESPath allows you to declaratively specify how to extract elements from a JSON document.

- [oauthlib](https://oauthlib.readthedocs.io/en/latest/) - A framework which implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework.

- [Pillow](https://pypi.org/project/Pillow/) - Python Imaging Library is a free and open-source additional library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats.

- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/) -  A popular PostgreSQL database adapter for the Python programming language.

- [python3-openid](https://pypi.org/project/python3-openid/) - A set of Python packages to support use of the OpenID decentralized identity system in applications.

- [pytz](https://pypi.org/project/pytz/) - Brings the Olson tz database into Python. This library allows accurate and cross platform timezone calculations using Python 2.4 or higher.

- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/) - Uses the Python Requests and OAuthlib libraries to provide an easy-to-use Python interface for building OAuth1 and OAuth2 clients. 

- [s3transfer](https://pypi.org/project/s3transfer/) - A Python library for managing Amazon S3 transfers.

- [sqlparse](https://pypi.org/project/sqlparse/) - A non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements.

- [stripe](https://pypi.org/project/stripe/) - A Python library for Stripe’s API.

## Testing

The testing data for this project can be found in a separate file called [TESTING.md](https://github.com/Johnny-Morgan/pickles/blob/master/TESTING.md).

## Credits

### Code

- The code for this project is based on the Code Institute's [Boutique Ado](https://www.youtube.com/watch?v=za5lGVvOEtw&t=126s&ab_channel=MediaUpload) Project.

- The code to change the carousel arrow colour was taken from [stackoverflow](https://stackoverflow.com/questions/46249541/change-arrow-colors-in-bootstraps-carousel).

- The code for the home page contact details layout was taken from the YouTube channel [Online Tutorials](https://www.youtube.com/watch?v=gggB0Nq5vBk&ab_channel=OnlineTutorials) and edited.

- The code to add a font awesome icon to an input field was taken from [stackoverflow](https://stackoverflow.com/questions/15988373/how-do-i-add-a-font-awesome-icon-to-input-field).

### Media

- The product and blog post images were taken from [pixababy](https://pixabay.com/).

- The site favicon was created using the website [favicon.io](https://favicon.io/favicon-generator/).

## Acknowledgements

My mentor Gerard McBride for his support and guidance during this project.

The Code Institute Slack community for their advice and tips.

Gilly McCrone for providing product descriptions and blog content.

Friends and family who tested the site.

> [Back to Top](#table-of-contents)