

run: build
	# java -cp lib/junit-4.13.2.jar:lib/hamcrest-core-1.3.jar:bin/ org.junit.runner.JUnitCore ClasseDeTeste
	java -cp lib/junit-4.13.2.jar:lib/hamcrest-core-1.3.jar:bin/ org.junit.runner.JUnitCore TestSoma

build: install
	#Classe a ser testada
	javac -d bin ClasseASerTestada.java zz/*.java

	#Classe de teste
	javac -d bin -cp lib/junit-4.13.2.jar:bin ClasseDeTeste.java TestSoma.java

clear:
	rm -rf bin

install:
	@wget -q -c -P lib --show-progress https://repo1.maven.org/maven2/junit/junit/4.13.2/junit-4.13.2.jar
	@wget -q -c -P lib --show-progress https://repo1.maven.org/maven2/org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar
