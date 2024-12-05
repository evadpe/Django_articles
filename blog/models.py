from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=50)  # Auteur du commentaire (max 50 caractères)
    text = models.TextField()  # Contenu du commentaire
    created_at = models.DateTimeField(auto_now_add=True)  # Horodatage de création

    def __str__(self):
        # Retourne une version tronquée (50 caractères max) du contenu du commentaire
        return f"{self.text[:50]}{'...' if len(self.text) > 50 else ''}"
