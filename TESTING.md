# Testing

## Testing User Stories

- As a **store owner**, I want to be able to:

    1. *Add a product, so that I can add new items to my store.*

        Store owners have access to a Product Admin page which contains a form that allows them to a add a new product to the store. 
        
        ![Add a Product Gif](docs/testing_gifs/add_product.gif)

    2. *Edit a product, so thas I can change the details of the product such as its price, description, image and other properties.*

        On the product info page for each product, an edit product button is displayed for store owners. Clicking this button directs the store owner to a form where they can edit the details of the product.

        ![Edit a Product Gif](docs/testing_gifs/edit_product.gif)

    3. Delete a product, so that I can remove items from my store that are no longer available.

        On the product info page for each product, a delete product button is displayed for store owners. Clicking this button opens a modal which askes the user if they wish to delete the product. Clicking the modal delete button removes the item from the store.

        ![Delete a Product Gif](docs/testing_gifs/delete_product.gif)

    4. Add a blog post, so that I can add new content to my blog page to help drive traffic to my store.

        On the blog page, an Add Blog Post button is displayed for store owners. Clicking the button directs the user to a new page where a form is displayed for adding a new blog post.

        ![Add a Blog Post Gif](docs/testing_gifs/add_blog_post.gif)

    5. Edit a blog post, so thas I can change the details of the blog such as its title, content, image and other properties. 

        In each blog post page, there is a button located below the blog post content, visible only to store owners. Clicking the button directs the user to a form where the blog post details can be edited.

        ![Add a Blog Post Gif](docs/testing_gifs/edit_blog_post.gif)

    6. Delete a blog post, so that I can remove blog posts that are outdated or irrelevent.

        In each blog post page, there is a button located below the blog post content, visible only to store owners. Clicking this button opens a modal which askes the user if they wish to delete the blog post. Clicking the modal delete button removes the blog post.

        ![Add a Blog Post Gif](docs/testing_gifs/delete_blog_post.gif)

    7. Delete a blog post comment, so that I can remove a comment that contains offensive content.

        There is a delete button under every blog post comment that is visible to only store owners. Clicking this button opens a modal which askes the user if they wish to delete the comment. Clicking the modal delete button deletes the comment.

        ![Add a Blog Post Gif](docs/testing_gifs/delete_comment.gif)
    
    8. Delete a product review, so that I can remove a review that contains offensive content.

        There is a delete button under every review that is visible to only store owners. Clicking this button opens a modal which askes the user if they wish to delete the review. Clicking the modal delete button deletes the review.

        ![Add a Blog Post Gif](docs/testing_gifs/delete_review.gif)




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