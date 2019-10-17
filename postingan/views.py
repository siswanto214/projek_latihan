from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Post, Kategori, Komentar

# Create your views here.
def post_list(request):
    postingan = Post.objects.all().order_by('tanggal_post')
    ini_kategori = Kategori.objects.all()
    context = {
        'postingan': postingan,
        'ini_kategori':ini_kategori,
    }
    return render(request, 'postingan/post_list.html', context)

def post_detail(request, pk):
    post=Post.objects.get(pk=pk)
    kategori = Kategori.objects.all()
    komentar = Komentar.objects.filter(postingan=pk)
    context = {
        'post': post,
        'komentar':komentar,
        'kategori':kategori,
    }
    return render(request, 'postingan/post_detail.html', context)
    if request.method == "POST":
        post_nya = Komentar(
            komentar=request.POST['komentar'],
            postingan=request.POST['id_post'],
        )
        post_nya.save()
        return redirect('komen_new', pk=post.pk)
    else:
    	post=get_object_or_404(Post,pk=pk)
    	context = {
    		'post': post,
    	}        
    return render(request, 'postingan/komen_new.html', context)

def post_filter(request):
    if request.method == "POST":
        id_kategori = request.POST['id_kategori']
        filter_kategori = Kategori.objects.get(id=id_kategori)
        if id_kategori != "1":
            postingan = Post.objects.filter(kategori=id_kategori)        
        else:    
            postingan = Post.objects.all()
        context = {
        'postingan':postingan,
        'filter_kategori': filter_kategori
        }
        return render(request, 'postingan/post_list.html', context)
    else:
        ini_kategori = Kategori.objects.all()
        context = {
            'ini_kategori': ini_kategori,            
        }
    return render(request, 'postingan/post_filter.html',context)

def post_new(request):
    if request.method == "POST":
        if 'id_kategori' in request.POST:
            id_kategori = request.POST['id_kategori']
        else:
            id_kategori = False
        ini_kategori = Kategori.objects.get(id=id_kategori)    
        post_nya = Post(
            penulis=request.POST['penulis'],
            judul=request.POST['judul'],
            isi=request.POST['isi'],
            tanggal_post=timezone.now(),
            tanggal_buat=timezone.now(),
            kategori=ini_kategori,
        )
        post_nya.save()
        return redirect('post_list')
    else:
        ini_kategori = Kategori.objects.filter()
        context = {
            'ini_kategori': ini_kategori
        }
    return render(request, 'postingan/post_new.html',context)

def post_edit(request, pk):
    postingan = Post.objects.get(pk=pk)
    if request.method == "POST":
        if 'id_kategori' in request.POST:
            id_kategori = request.POST['id_kategori']
        else:
            id_kategori = False
        ini_kategori = Kategori.objects.get(id=id_kategori) 
        postingan.penulis=request.POST['penulis']
        postingan.judul=request.POST['judul']
        postingan.isi=request.POST['isi']
        postingan.kategori=ini_kategori
        postingan.save()

        return redirect('post_list')
    else:
        ini_kategori = Kategori.objects.all()
        postingan = Post.objects.get(pk=pk)
        context = {
            'ini_kategori': ini_kategori,
            'postingan':postingan,
        }
    return render(request, 'postingan/post_edit.html',context)

def post_delete(request, pk):
    Post.objects.filter(pk=pk).delete()
    return redirect('post_list')

def komen_new(request):
    if request.method == "POST":
    	id_post = request.POST['postingan']
    	postingan = Post.objects.get(id=id_post)
    	komen_nya = Komentar(
        	postingan=postingan,
        	komentar=request.POST['komentar'],)
    	komen_nya.save()
    	return redirect('post_list')
    else:
        postingan = Post.objects.all()
        context = {
            'postingan': postingan,
        }
    return render(request, 'postingan/komen_new.html',context)

def komen_edit(request, pk):
    komen = Komentar.objects.get(pk=pk)
    if request.method == "POST":
        komen.komentar=request.POST['komentar']
        komen.save()
        return redirect('post_list')
    else:
        komen = Komentar.objects.get(pk=pk)
        context = {
            'komen':komen,
        }
    return render(request, 'postingan/komen_edit.html',context)

def komen_delete(request, pk):
    Komentar.objects.filter(pk=pk).delete()
    return redirect('post_list')

def kategori_list(request):
    ini_kategori = Kategori.objects.all().order_by('id')
    context = {
        'ini_kategori':ini_kategori,
    }
    return render(request, 'postingan/kategori_list.html', context)

def kategori_new(request):
    if request.method == "POST":   
        post_nya = Kategori(
            nama_kategori=request.POST['nama_kategori'],
        )
        post_nya.save()
        return redirect('post_list')
    else:
        postingan = Kategori.objects.all()
        context = {
            'postingan': postingan,
        }
    return render(request, 'postingan/kategori_new.html',context)

def kategori_edit(request, pk):
    kat = Kategori.objects.get(pk=pk)
    if request.method == "POST":
        kat.nama_kategori=request.POST['nama_kategori']
        kat.save()
        return redirect('post_list')
    else:
        kat = Kategori.objects.get(pk=pk)
        context = {
            'kat':kat,
        }
    return render(request, 'postingan/kategori_edit.html',context)

def kategori_delete(request, pk):
    Kategori.objects.filter(pk=pk).delete()
    return redirect('post_list')