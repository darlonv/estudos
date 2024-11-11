
all: run

#Obtém os nomes das classes de testes, sem a extensão
DIRECTORY := tests
FILENAMES := $(shell for file in $(DIRECTORY)/*; do basename $${file%.*}; done)


test: build-test
	#Executando testes..
	java -cp lib/junit-4.13.2.jar:lib/hamcrest-core-1.3.jar:bin/ org.junit.runner.JUnitCore $(FILENAMES)

build-test: install build
	#Compilando testes..
	javac -d bin -cp lib/junit-4.13.2.jar:bin tests/*.java

build:
	#Compilando..
	javac -d bin Main.java arquivos/*.java

run: build
	#Executando..
	java -cp bin Main

clear:
	#Limpando..
	rm -rf bin

install:
	#Obtendo Junit e Hamcrest
	#@wget -q -c -P lib --show-progress https://repo1.maven.org/maven2/junit/junit/4.13.2/junit-4.13.2.jar
	#@wget -q -c -P lib --show-progress https://repo1.maven.org/maven2/org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar
