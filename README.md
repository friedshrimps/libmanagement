
# Gestion d'une bibliothèque



## Introduction

Gérer une bibliothèque peut s'avérer complexe, surtout en ce qui concerne le suivi des collections de livres. Notre application permet de stocker facilement les informations relatives aux livres, de les organiser et de les localiser rapidement, offrant ainsi aux bibliothécaires un système efficace pour suivre les livres en temps réel, vérifier leur disponibilité et leur emplacement dans la bibliothèque. En outre, notre application vise à satisfaire les besoins des utilisateurs en leur offrant un accès en ligne aux informations détaillées sur les livres disponibles, ainsi qu'à la possibilité de réserver des livres en ligne. En fin de compte, notre application offre une expérience utilisateur optimale pour tous les utilisateurs, améliorant ainsi la gestion des collections de livres dans toutes les bibliothèques.
## Fonctionnalités
Les fonctionnalités de l'application de gestion deq livres comprennent :

- Stockage et gestion d'informations sur les livres, y compris les titres, les auteurs, les années de publication et les images des couvertures de livres.

- Organisation des livres par titres, auteurs ou années pour faciliter la recherche.

- Ajout, modification et suppression de livres : les administrateurs peuvent facilement ajouter de nouveaux livres à la collection,
modifier les informations existantes et supprimer les livres obsolètes.

- Interface utilisateur conviviale pour les bibliothécaires et les emprunteurs.

## Authors

- Elfeddani Aya - [@Aya-elfe](https://www.github.com/Aya-elfe)

- Norelyakine Aya - [@friedshrimps](https://www.github.com/friedshrimps)


## Conception

### UML

- Diagramme de cas d'utilisation


![use_case](https://user-images.githubusercontent.com/121770088/236561163-36431cd4-6354-430e-920f-019abc64dd8c.PNG)


- Diagramme de classes

![classeb](https://user-images.githubusercontent.com/121770088/236561586-25296654-5ed1-4e7f-a7aa-804655f22a2d.PNG)


## Interfaces

### Administrateur:

L'administrateur principal a , par défaut, été inscrit par le développeur. Ce-ci dit, son username est 'admin0' et son mot de passe et 'admin0'. C'est l'administrateur principal qui pourrait ajouter un ou plusieurs admins en premier lieu, qui à leurs tours pourraient faire de même.

#### LOGIN
Le client et l'administrateur peuvent tous les deux accéder à l'application via la même page Login.

![image](https://user-images.githubusercontent.com/121770088/236578398-225b5ca7-7570-4967-b307-3d9c0231fda2.png)

Pour les différencier et bien organizer cet étape, un 'CheckButton' fut implémenté. Alors la table admin dans la base de données va être vérifier si le bouton est coché. Au cas où les données entrées sont effectivement présentes, on pourra accéder en tant qu'administrateur, sinon un message d'erreur va se génerer.

![image](https://user-images.githubusercontent.com/121770088/236564144-f50b4ae1-b52a-46d4-b63f-1426e8b002fa.png)

L'administrateur sera redirigé vers la page principale de la bibliothèque.
Ici l'administrateur peut effectuer la recherche et le CRUD.

![image](https://user-images.githubusercontent.com/121770088/236582361-0aadef29-c730-4693-bf38-99807fda79a4.png)



 ##### Affichage des livres:
 
 Les livres sont listés sous forme de 'cards frame'. Les informations affichées sont: Titre, Auteur, Image de couverture et Id.
 
 ![image](https://user-images.githubusercontent.com/121770088/236570548-645ee6c2-c398-4903-9e46-cd85ec15cce5.png)
 
 On a ajoutés deux boutons dans chaque 'card' pour la suppression et modification. 
 
![image](https://user-images.githubusercontent.com/121770088/236570623-43a3d9e4-0522-4270-b60d-016cf8fa818d.png)

- Suppression:

    On appelle la fonction delete_livre()
    
    ![image](https://user-images.githubusercontent.com/121770088/236570770-aae5f42b-04ed-475f-9be8-f772015b281a.png)
    
    Celle-ci va importer delete.
    
    ![image](https://user-images.githubusercontent.com/121770088/236571352-a792ebe6-8f53-4bb6-ad07-4b251cd2cb4f.png)
    
    L'administrateur doit saisir l'Id affiché du livre qu'il souhaite supprimer.
    
    -> Fonction pour obtenir l'Id saisi par l'administrateur
    
    ![image](https://user-images.githubusercontent.com/121770088/236571671-fa794cb0-e003-4775-9103-2127b79da1a9.png)
    
    -> Fonction pour supprimer le livre de la Base de données
    
    ![image](https://user-images.githubusercontent.com/121770088/236571871-013b73c8-89a4-4628-91ef-e0e4dc5ef943.png)

- Modification

     On appelle la fonction on_update_click().
     
    ![image](https://user-images.githubusercontent.com/121770088/236572172-792cdcc1-bc88-44c1-974e-31001ece92be.png)
    
    Une fenêtre TopLevel est créée, et les informations du livre qu'on souhaite modifier sont affichées dans les 'entries'.
    
    ![image](https://user-images.githubusercontent.com/121770088/236572597-f32cd344-1043-4115-afee-af827cc32fb8.png)
    
    
    ![image](https://user-images.githubusercontent.com/121770088/236572301-9abe531e-329b-4cb6-9e89-4f76a7b524ce.png)
    
    Une fois le bouton 'Modifier' clické, les données sont obtenues et la base de données est mise à jour.
    
    ![image](https://user-images.githubusercontent.com/121770088/236572835-398260d6-1456-438b-9cf4-77a1adf50d5b.png)

    -> Après Modification:
    
    ![image](https://user-images.githubusercontent.com/121770088/236584705-d44b0b14-fc3e-4d67-b895-d72a92a62d80.png)


##### Fonction Recherche:

L'admin peut saisir soit le titre, l'auteur ou l'annee pour que les livres concernés soient affichés.

![image](https://user-images.githubusercontent.com/121770088/236565208-b83ab991-0fea-483f-aa3a-7e5f2fc4871b.png)

##### Fonction Ajout Livres:

![image](https://user-images.githubusercontent.com/121770088/236574635-9787cbbc-24c9-4f53-ac54-1659c39de5b0.png)

Une fois l'administrateur clique sur le bouton 'Add Book', il est redirigé vers une autre page pour l'ajout.

![image](https://user-images.githubusercontent.com/121770088/236574865-be4692b4-42ec-4e4d-aee5-5c3823f9d0bf.png)

L'administrateur saisit les informations du livre qu'il souhaite ajouté.


- Naviguer Fichiers pour soumettre une image:

![image](https://user-images.githubusercontent.com/121770088/236574985-d9e4ba19-6948-489a-b9e4-8a005ba84332.png)

Une fois les données saisies, si le bouton d'ajout est cliqué toutes les informations seront insérées dans la table Livre de la base de données.

![image](https://user-images.githubusercontent.com/121770088/236575051-53f9aef5-238c-4b56-b903-3a66aa47cf0d.png)

##### Fonction Ajout Admin:

Par contre, si l'admin clique sur le bouton 'Add Admin', il sera dirigé vers une autre page.

![image](https://user-images.githubusercontent.com/121770088/236575443-4d330d2c-c3c9-409f-b7a9-a3a7ef8ac303.png)



### Client:

#### Login:

Comme pour l'administrateur, l'utilisateur saisi ses informations s'il est inscrit, mais ne coche pas sur le 'CheckButton' réservé à l'admin.

![image](https://user-images.githubusercontent.com/121770088/236578376-10fbe12d-863d-419e-9671-6c6827632b75.png)


#### Inscription:

Le client tout d'abord se retrouve devant une page d'inscription. 

![image](https://user-images.githubusercontent.com/121770088/236575793-11ceea19-3c23-4d64-99b7-ffe8fa5915a6.png)

S'il est déjà inscrit, il peut tout simplememt cliquer sur le lien Login. Sinon, il saisi toutes les informations et rempli tous les champs. 

Si son nom d'utilisateur existe déjà, ses mots de passes sont différents, ou bien les champs ne sont pas tous remplis, un message d'erreur se génere.

![image](https://user-images.githubusercontent.com/121770088/236576322-aff05b25-bd2b-4c95-b7da-5970f0e0745e.png)

On securise le mot de passe de l'utilisateur, par bcrypt:

              hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
              
Ensuite, le nom et le mot de passe (hashed) sont insérés dans la base de données.

Un message de succès est affiché, on redirige l'utilisateur ensuite vers la page d'accueil de la bibliothèque.

![image](https://user-images.githubusercontent.com/121770088/236576953-a6d66bf8-f4c6-443b-b0c1-e14f66cc7f28.png)




#### Page d'accueil:


![image](https://user-images.githubusercontent.com/121770088/236582259-91b7168b-b372-4b4c-86ec-4fee28b66c03.png)

L'utilisateur peut effectuer une recherche par auteur, titre ou année. 

ps: Le bouton 'plus' est originellement implémenter pour afficher une section de choix pour l'utilisateur, où il pourra sélectionner s'il souhaiterait acheter, emprunter, ou ajouter a son 'Cart'.

