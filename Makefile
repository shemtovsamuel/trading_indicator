##
## EPITECH PROJECT, 2021
## undefined
## File description:
## Makefile
##


SRC = ./src/

NAME = groundhog

$(NAME) :
	cp $(SRC)main.py ./
	mv main.py groundhog
	chmod +x groundhog

all : $(NAME)

clean:
	rm -f src/*.o
	rm -f tests/*.o
	rm -f *.html
	rm -f *.css

fclean: clean
	rm -f $(NAME)
	rm -f unit_tests

re:	fclean all

.PHONY: all clean fclean re