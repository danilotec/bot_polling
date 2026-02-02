from bot import main, verify_and_send_message

urls = [
    'https://omnisistems.com.br',
    'https://bellafly.omnisistems.com.br',
    'https://crmonitoramento.omnisistems.com.br'
]

main(verify_and_send_message, urls)
