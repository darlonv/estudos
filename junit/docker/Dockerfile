# Usar uma imagem base do OpenJDK
FROM openjdk:11-jdk

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o código-fonte para o contêiner
COPY . .

# Baixar o JUnit e suas dependências
RUN curl -L -o junit-platform-console-standalone.jar https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console-standalone/1.8.2/junit-platform-console-standalone-1.8.2.jar 


# Comando para executar os testes (substitua TestClass pelo nome da sua classe de teste)
CMD ["java", "-jar", "junit-platform-console-standalone.jar", "--class-path", ".", "--scan-class-path"]