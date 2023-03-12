import instaloader
import getpass
import re

carregar = instaloader.Instaloader()

userName = input("Qual o seu nome de ususario")
senha = getpass("Senha:")

carregar.login(userName, senha)

url = input("URL: ")

separadorBarra = r"\/p\/([^\/]*)/"

encontrou = re.search(separadorBarra, url)

if encontrou:
    print("Baixando: ", encontrou.group(1), "....")

    post = instaloader.Post.from_shortcode(carregar.context, encontrou.group(1))
    carregar.dowload_post(post, "downloads")
