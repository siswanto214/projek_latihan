from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

# Create your models here.

#model untuk membuat tabel Kategori
class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=20)

#model untuk membuat data post di tabel Postingan
class Post(models.Model):
    penulis = models.CharField(max_length=200)
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    tanggal_buat = models.DateTimeField(default=timezone.now)
    tanggal_post = models.DateTimeField(blank=True, null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.judul

#model untuk membuat tabel Komentar
class Komentar(models.Model):
    postingan = models.ForeignKey(Post, on_delete=models.CASCADE)
    komentar = models.TextField()

    def __str__(self):
        return self.komentar