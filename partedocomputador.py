#  https://www.twilio.com/docs/voice/twinl
	from secrets import account_sid, token
	from twilio.rest import Client 
	
	import serial
	button = serial.Serial(0)  // a funcao de botao é receber o sinal do usuario

	print("Aguardando o pressionamento do botao")
	
	while (button==1){
		
	account_sid = ""  
	auth_token = ""
	meu_numero = "" //informar numero que ira receber a ligacao
	numero_twilio = ""  //preencher o numero disponivel no site do Twilio
	
	//utilizar o site Make Outbound Phone Calls with Python
	
	Client = Client(accound_sid, token)
	mensagem = ""
	<Response>
	<Say language=pt-BR">
	Voce acaba de receber um sinal da muleta assistida   //mensagem que sera trasmitida por audio 
	</Say>
	</Response>
	
	ligacao = client.calls.create()
	  to = meu_numero,
	  from = numero_twilio //este é o numero que foi habilitado no site do Twilio
	  twinl=  "" //forma de escrever a mensagem que o Twilio disponibiliza para voce
	
	}
	}
