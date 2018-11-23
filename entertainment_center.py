import media
import fresh_tomatoes


narradores_de_jave = media.Movie("Narradores de Javé", "Ao saber que Javé pode desaparecer sob as águas de uma hidrelétrica, os moradores do vilarejo decidem escrever sua história e transformar o local em patrimônio a ser preservado.", "https://upload.wikimedia.org/wikipedia/pt/3/35/Narradores_de_Jav%C3%A9.jpg", "https://www.youtube.com/watch?v=GlaFRraqeOg")

era_o_hotel_cambridge = media.Movie("Era o hotel cambridge", "Refugiados recém-chegados ao Brasil dividem com um grupo de sem-tetos um velho edifício abandonado no centro de São Paulo. Os novos moradores do prédio têm que lidar com seus dramas pessoais e aprender a conviver com pessoas que, apesar de diferentes, enfrentam juntos a vida nas ruas.", "http://www.atoupeira.com.br/wp-content/uploads/2016/10/Era-o-Hotel-Cambridge-Festival-do-Rio.png", "https://www.youtube.com/watch?v=a5EQUG-RMI8")

o_auto_da_compadecida = media.Movie("O auto da compadecida", "O filme mostra as aventuras de João Grilo e Chicó, dois nordestinos pobres que vivem de golpes para sobreviver. Eles estão sempre enganando o povo de um pequeno vilarejo no sertão da Paraíba, inclusive o temido cangaceiro Severino de Aracaju, que os persegue pela região. Somente a aparição da Nossa Senhora poderá salvar esta dupla.", "https://upload.wikimedia.org/wikipedia/pt/b/bf/O_auto_da_compadecida.jpg", "https://www.youtube.com/watch?v=XPuMu_ENzlg")

o_homem_que_virou_suco = media.Movie("O homem que virou suco", "Um poeta popular do Nordeste chega a São Paulo, sobrevivendo apenas de suas poesias e folhetos. Porém sua vida muda quando ele é confundido com o operário de uma multinacional que matou o patrão em uma festa.", "http://d3swacfcujrr1g.cloudfront.net/img/uploads/2000/01/001151007019.jpg", "https://www.youtube.com/watch?v=FKo69RAElJg")

central_do_brasil = media.Movie("Central do Brasil", "Dora, uma amargurada ex-professora, ganha a vida escrevendo cartas para pessoas analfabetas, que ditam o que querem contar às suas famílias. Ela embolsa o dinheiro sem sequer postar as cartas. Um dia, Josué, o filho de nove anos de idade de uma de suas clientes, acaba sozinho quando a mãe é morta em um acidente de ônibus. Ela reluta em cuidar do menino, mas se junta a ele em uma viagem pelo interior do Nordeste em busca do pai de Josué, que ele nunca conheceu.", "https://upload.wikimedia.org/wikipedia/pt/2/29/Central_do_Brasil_poster.jpg", "https://www.youtube.com/watch?v=xmMR46HsaBc")

kenoma = media.Movie("Kenoma", "Um artesão de um pequeno povoado tenta construir uma máquina que trabalhe por ela mesma - de movimento perpétuo -, mas um poderoso proprietário de terras lhe impõe um prazo impossível de ser cumprido.", "https://upload.wikimedia.org/wikipedia/pt/2/2a/Kenoma.jpg", "https://www.youtube.com/watch?v=tVHfI4TFCeY")



#cria uma lista com instâncias da classe Movie do arquivo media.py
movies = [narradores_de_jave, era_o_hotel_cambridge, o_auto_da_compadecida, o_homem_que_virou_suco, central_do_brasil, kenoma]

# inicia a função open_movies_page do arquivo fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
