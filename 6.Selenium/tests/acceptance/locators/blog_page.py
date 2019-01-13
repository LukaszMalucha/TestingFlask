from selenium.webdriver.common.by import By


class BlogPageLocators:
    NEW_POST_LINK = By.ID, 'add-post-link'
    POSTS_SECTION = By.ID, 'posts'
    POST = By.CLASS_NAME, 'post-link'
