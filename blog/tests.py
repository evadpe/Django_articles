from django.test import TestCase, Client
from django.urls import reverse
from .models import BlogPost, Comment
from django.test import TestCase, Client
from django.urls import reverse
from .models import BlogPost, Comment

# Tests pour les articles de blog
class BlogPostTests(TestCase):
    def test_create_blog_post(self):
        post = BlogPost.objects.create(title="Test Title", content="Test Content")
        self.assertEqual(post.title, "Test Title")
        self.assertEqual(post.content, "Test Content")
        self.assertIsNotNone(post.created_at)

    def test_edit_blog_post(self):
        post = BlogPost.objects.create(title="Old Title", content="Old Content")
        post.title = "New Title"
        post.content = "New Content"
        post.save()
        updated_post = BlogPost.objects.get(pk=post.pk)
        self.assertEqual(updated_post.title, "New Title")
        self.assertEqual(updated_post.content, "New Content")

    def test_delete_blog_post(self):
        post = BlogPost.objects.create(title="To be deleted", content="Delete this content")
        post_id = post.pk
        post.delete()
        with self.assertRaises(BlogPost.DoesNotExist):
            BlogPost.objects.get(pk=post_id)


# Tests pour les commentaires
class CommentTests(TestCase):
    def test_add_comment(self):
        post = BlogPost.objects.create(title="Post with comments", content="Content")
        comment = Comment.objects.create(post=post, author="Test Author", text="Test Comment")
        self.assertEqual(comment.author, "Test Author")
        self.assertEqual(comment.text, "Test Comment")
        self.assertEqual(comment.post, post)

    def test_edit_comment(self):
        post = BlogPost.objects.create(title="Post", content="Content")
        comment = Comment.objects.create(post=post, author="Author", text="Old Comment")
        comment.text = "Updated Comment"
        comment.save()
        updated_comment = Comment.objects.get(pk=comment.pk)
        self.assertEqual(updated_comment.text, "Updated Comment")

    def test_delete_comment(self):
        post = BlogPost.objects.create(title="Post", content="Content")
        comment = Comment.objects.create(post=post, author="Author", text="To be deleted")
        comment_id = comment.pk
        comment.delete()
        with self.assertRaises(Comment.DoesNotExist):
            Comment.objects.get(pk=comment_id)


# Tests pour les vues
class BlogPostViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list_view(self):
        BlogPost.objects.create(title="Test Post 1", content="Content 1")
        BlogPost.objects.create(title="Test Post 2", content="Content 2")
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post 1")
        self.assertContains(response, "Test Post 2")

    def test_post_detail_view(self):
        post = BlogPost.objects.create(title="Test Post", content="Content")
        response = self.client.get(reverse('post_detail', args=[post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
        self.assertContains(response, "Content")

    def test_create_post_redirect(self):
        response = self.client.post(reverse('create_post'), {'title': 'New Post', 'content': 'Content'})
        self.assertEqual(response.status_code, 302)  # Redirection
        self.assertTrue(BlogPost.objects.filter(title="New Post").exists())

    def test_delete_post_redirect(self):
        post = BlogPost.objects.create(title="Post to delete", content="Content")
        response = self.client.post(reverse('delete_post', args=[post.pk]))
        self.assertEqual(response.status_code, 302)  # Redirection
        self.assertFalse(BlogPost.objects.filter(pk=post.pk).exists())
