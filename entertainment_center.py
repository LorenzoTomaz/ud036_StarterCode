import media
import fresh_tomatoes


narradores_de_jave = media.Movie("narradores de jave", "Ao saber que Javé pode desaparecer sob as águas de uma hidrelétrica, os moradores do vilarejo decidem escrever sua história e transformar o local em patrimônio a ser preservado.", "https://upload.wikimedia.org/wikipedia/pt/3/35/Narradores_de_Jav%C3%A9.jpg", "https://www.youtube.com/watch?v=GlaFRraqeOg")

era_o_hotel_cambridge = media.Movie("era o hotel cambridge", "Refugiados recém-chegados ao Brasil dividem com um grupo de sem-tetos um velho edifício abandonado no centro de São Paulo. Os novos moradores do prédio têm que lidar com seus dramas pessoais e aprender a conviver com pessoas que, apesar de diferentes, enfrentam juntos a vida nas ruas.", "http://www.atoupeira.com.br/wp-content/uploads/2016/10/Era-o-Hotel-Cambridge-Festival-do-Rio.png", "https://www.youtube.com/watch?v=a5EQUG-RMI8")

o_auto_da_compadecida = media.Movie("O auto da compadecida", "O filme mostra as aventuras de João Grilo e Chicó, dois nordestinos pobres que vivem de golpes para sobreviver. Eles estão sempre enganando o povo de um pequeno vilarejo no sertão da Paraíba, inclusive o temido cangaceiro Severino de Aracaju, que os persegue pela região. Somente a aparição da Nossa Senhora poderá salvar esta dupla.", "https://upload.wikimedia.org/wikipedia/pt/b/bf/O_auto_da_compadecida.jpg", "https://www.youtube.com/watch?v=XPuMu_ENzlg")

o_homem_que_virou_suco = media.Movie("O homem que virou suco", "Um poeta popular do Nordeste chega a São Paulo, sobrevivendo apenas de suas poesias e folhetos. Porém sua vida muda quando ele é confundido com o operário de uma multinacional que matou o patrão em uma festa.", "http://d3swacfcujrr1g.cloudfront.net/img/uploads/2000/01/001151007019.jpg", "https://www.youtube.com/watch?v=FKo69RAElJg")

#cria uma lista com instâncias da classe Movie do arquivo media.py
movies = [narradores_de_jave, era_o_hotel_cambridge, o_auto_da_compadecida, o_homem_que_virou_suco]

# inicia a função open_movies_page do arquivo fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
