Instrukcja odpalenia aplikacji localnie pod systemem operacyjnym Linux

W terminalu utworz nowy katalog w ktorym znajdzie sie projekt:

	mkdir token_api

nastepnie postepuj zgodnie z punktami

	1. cd token_api
	2. git init
	3. git clone https://github.com/mario-pe/TokenAuthAPi.git
	4. cd user_token 
	5. python manage.py test - polecenie uruchamia testy jednostkowe
	6. python manage.py runserver - polecenie uruchamia server localny

Instrukcja do API 

	Local:

	Aby pobrać szczegóły dotyczące obecnie zalogowanego użytkownika należy użyć metoda get przslac zapytanie na url  https://shielded-anchorage-20223.herokuapp.com/users/users/me/   autentykacja za pomocą wygenerowanego token’u 
	
	W celu rejestracji nowego użytkownika w ciele zapytania powinny znaleźć się: email, nazwa użytkownika oraz hasło. Informacje nalezy przeslac za pomocą metody PUT na adres https://shielded-anchorage-20223.herokuapp.com/users/register/
	
	Pobranie informacji o wszystkich uzytkownikach odbywa się za pomocą metody GET na adresie https://shielded-anchorage-20223.herokuapp.com/users/users/  autentykacja po przez token.
	 

	W celu pobrania token’u nalezy przeslać swój email wraz z haslem, metoda: POST na adres https://shielded-anchorage-20223.herokuapp.com/users/login/ 
