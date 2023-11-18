# Ordenacao-de-Numeros
#### <div align="center"> Uma pequena aplicação de ordenação de numeros </div> <br>

![Imagem ilustrativa do QuickNotes](https://images.prismic.io/voitto-blog/e60233c8-cce8-449b-b2c7-417319063f9a_Jogo+dos+n%C3%BAmeros+2..jpg) 

### <div align="center"> Esse codigo foi criado para uma atividade da universidade. </div>

O Usuario escolhe a quantidade de numeros que deseja por na lista, após isso o sistema pede pra inserir os numeros, podendo ser int ou float, depois de adicionar a quantidade dos numeros que o sistema pediu, aparece os mesmo numeros na saida em ordem digitada e ordenada

## ‼️ Problemas encontrados:
 1- O numero era armazenado mesmo quando dava erro, nisso quando o loop rodava pedindo a inserção certa, os numeros armazenados em erro aparecia junto com o certo Veja 👉🏼[Print](https://drive.google.com/file/d/1kLhuY9HzYpLtc93xxru5XcMsPOzT1DwT/view?usp=sharing) <br> <br>
 1.1 - pra resolver tive que colocar o metodo .clear() no except. <br>
 ~~~Python 
     except ValueError:
        print("\nÉ permitido somente numeros, tente novamente!\n")
        lista_com_ordem.clear()
        lista_sem_ordem.clear()
 ~~~

## 🚀 Funcionalidades
 1- O usuario é capaz de escolher a quantidade de numeros; <br>
 2- Metodo .join para tirar os colchetes na saida do código <br>
 3- O sitema não permite colocar letras, simbolos, ou no caso do float a virgula.

## 📚 Requisitos
 Python 3.11

 ## 📞 Contato

- Nome: Jonathan Oliveira
- Email: oliveirapersonnel@gmail.com
- LinkedIn: [@Jonathan-Olliveira](https://www.linkedin.com/in/jonathan-olliveira/)
- GitHub: @Jonathan-Olliveira

---
