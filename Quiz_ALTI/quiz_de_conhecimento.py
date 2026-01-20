# Contador de jogadas online
import requests

resposta_certa_fÃ¡cil=resposta_errada_fÃ¡cil=resposta_certa_mÃ©dio=resposta_errada_mÃ©dio=resposta_certa_difÃ­cil=resposta_errada_difÃ­cil=0
print('=='*30)
print(f'{'BEM-VINDO AO MUNDO DO CONHECIMENTO "QUIZ ALTI"':^60}')
print('=='*30)
    
while True:
    print('MENU PRINCIPAL:\n[1] Jogar Quiz\n[2] Sair')
    escolha_no_menu=int(input('\nEscolha uma opÃ§Ã£o: '))
    if escolha_no_menu == 1:
        # Registra jogada no contador (silencioso se falhar)
        try:
            requests.get('https://api.countapi.xyz/hit/alti-quiz/jogadas', timeout=2)
        except:
            pass
        
        nome=str(input('\nðŸ‘‰ Diga o seu nome: '))
        print(f'\n OlÃ¡ {nome}! Escolha a dificuldade:\n',
        '[1] FÃ¡cil(10 pontos por acerto)\n',
        '[2] MÃ©dio(20 pontos por acerto)\n',
        '[3] DifÃ­cil(30 pontos por acerto)')
        escolha_de_jogo=int(input('\nSua escolha: '))
        
        if escolha_de_jogo == 1:# FÃ¡cil ronda1
            print('=='*30)
            print(f'{'MODO FÃCIL - 10 PERGUNTAS':^30}')
            print('=='*30,'\n')
            print('PERGUNTA 1/10\nQual jogador tem 8 bolas de ouro?\n',
            'a) C.Ronaldo\n',
            'b) Neymar Jr\n',
            'c) Messi\n',
            'd) Lamine Yamal')
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'c':
                resposta_certa_fÃ¡cil+=1
                print(f'\nâœ… CORRETO! +10 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_fÃ¡cil*10} pontos.\n')
            else:
                resposta_errada_fÃ¡cil+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')
                
            print('PERGUNTA 2/10\nQuem criou o "QUIZ ALTI?"\n'
            'a) Nelson Mandela\n',
            'b) AmÃ­lcar Cabral\n',
            'c) Agostinho Neto\n',
            'd) Aleluia Nhaga Imbali')
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'd':
                resposta_certa_fÃ¡cil+=1
                print(f'\nâœ… CORRETO! +10 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_fÃ¡cil*10} pontos.\n')
            else:
                resposta_errada_fÃ¡cil+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')
                
            print('PERGUNTA 3/10\nQuanto Ã© raiz cÃºbica de dois (âˆ›8)?\n',
            'a) 6\n',
            'b) 2\n',
            'c) 3+2\n',
            'd) 5')
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'b':
                resposta_certa_fÃ¡cil+=1
                print(f'\nâœ… CORRETO! +10 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_fÃ¡cil*10} pontos.\n')
            else:
                resposta_errada_fÃ¡cil+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')
                
            print('PERGUNTA 4/10\nQuem pintou a Monalisa?\n',
            'a) PitÃ¡goras\n',
            'b) Leonardo da Vinci\n',
            'c) Immanuel Kant\n',
            'd) AristÃ³teles')
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'b':
                resposta_certa_fÃ¡cil+=1
                print(f'\nâœ… CORRETO! +10 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_fÃ¡cil*10} pontos.\n')
            else:
                resposta_errada_fÃ¡cil+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')
                
            print('PERGUNTA 5/10\nQual Ã© a capital de Portugal?\n',
            'a) Madrid\n',
            'b) Roma\n',
            'c) Lisboa\n',
            'd) Paris')
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'c':
                resposta_certa_fÃ¡cil+=1
                print(f'\nâœ… CORRETO! +10 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_fÃ¡cil*10} pontos.\n')
            else:
                resposta_errada_fÃ¡cil+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')
                
            print('PERGUNTA 6/10\nQual Ã© o maior planeta do sistema solar?\n',
            'a) JÃºpiter\n',
            'b) Saturno\n',
            'c) Marte\n',
            'd) Terra')
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'a':
                resposta_certa_fÃ¡cil+=1
                print(f'\nâœ… CORRETO! +10 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_fÃ¡cil*10} pontos.\n')
            else:
                resposta_errada_fÃ¡cil+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')
                
            print('PERGUNTA 7/10\nQual dessas Ã© um meio de transporte?\n',
            'a) Banana\n',
            'b) Carro\n',
            'c) Sapato\n',
            'd) Cadeira')
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'b':
                resposta_certa_fÃ¡cil+=1
                print(f'\nâœ… CORRETO! +10 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_fÃ¡cil*10} pontos.\n')
            else:
                resposta_errada_fÃ¡cil+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')
                
            print('PERGUNTA 8/10\nQual Ã© o idioma oficial da GuinÃ©-Bissau?\n',
            'a) Espanhol\n',
            'b) Criolo da GuinÃ©-Bissau\n',
            'c) FrancÃªs\n',
            'd) PortuguÃªs')
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'd':
                resposta_certa_fÃ¡cil+=1
                print(f'\nâœ… CORRETO! +10 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_fÃ¡cil*10} pontos.\n')
            else:
                resposta_errada_fÃ¡cil+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')
                
            print('PERGUNTA 9/10\nQual Ã© a cor do sol?\n',
            'a) Branco\n',
            'b) Amarelo\n',
            'c) Preto\n',
            'd) Vermelho')
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'a':
                resposta_certa_fÃ¡cil+=1
                print(f'\nâœ… CORRETO! +10 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_fÃ¡cil*10} pontos.\n')
            else:
                resposta_errada_fÃ¡cil+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')
                
            print('PERGUNTA 10/10\nQual animal Ã© conhecido como rei da selva?\n',
            'a) Elefante\n',
            'b) Tigre\n',
            'c) LeÃ£o\n',
            'd) Urso')
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'c':
                resposta_certa_fÃ¡cil+=1
                print(f'\nâœ… CORRETO! +10 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_fÃ¡cil*10} pontos.\n')
            else:
                resposta_errada_fÃ¡cil+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')
                print('...\n')
            print('=='*30)
            print(f'{'RESULTADO FINAL':^30}')
            print('=='*30)
            print(f'Nome: {nome}\n',
            f'Acertos: {resposta_certa_fÃ¡cil}/10\n',
            f'Erros: {resposta_errada_fÃ¡cil}/10\n',
            f'PontuaÃ§Ã£o final: {resposta_certa_fÃ¡cil*10}')
            if resposta_certa_fÃ¡cil*10==10:
                print(f'ClassificaÃ§Ã£o:\033[93mâ˜…\033[0m Tentativa\n')
            elif resposta_certa_fÃ¡cil*10==20:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸ\033[0m Ruim')
            elif resposta_certa_fÃ¡cil*10==30:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸâ˜…\033[0m Regular\n')
            elif resposta_certa_fÃ¡cil*10==40:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸðŸŒŸ\033[0m Fraco\n')
            elif resposta_certa_fÃ¡cil*10==50:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸðŸŒŸâ˜…\033[0m AceitÃ¡vel\n')
            elif resposta_certa_fÃ¡cil*10==60:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸðŸŒŸðŸŒŸ\033[0m Bom\n')
            elif resposta_certa_fÃ¡cil*10==70:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸðŸŒŸðŸŒŸâ˜…\033[0m Muito Bom\n')
            elif resposta_certa_fÃ¡cil*10==80:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸðŸŒŸðŸŒŸðŸŒŸ\033[0m Ã“timo\n')
            elif resposta_certa_fÃ¡cil*10==90:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸðŸŒŸðŸŒŸðŸŒŸâ˜…\033[0m Quase Excelente\n')
            elif resposta_certa_fÃ¡cil*10==100:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸðŸŒŸðŸŒŸðŸŒŸðŸŒŸ\033[0m Excelente\n')
            else:
                print('ClassificaÃ§Ã£o: Sem estrela ðŸ˜‹ Estude mais\n')

        elif escolha_de_jogo==2:# MÃ©dio ronda1
            print('=='*30)
            print(f'{'MODO MÃ‰DIO - 10 PERGUNTAS':^30}')
            print('=='*30)
            print('\nPERGUNTA 1/10\nQual Ã© o elemento quÃ­mico representado pelo sÃ­mbolo "Na"?\n',
            'a) NitrogÃªnio\n',
            'b) SÃ³dio\n',
            'c) NiÃ³bio\n',
            'd) NeÃ´nio')
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'b':
                resposta_certa_mÃ©dio+=1
                print(f'\nâœ… CORRETO! +20 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_mÃ©dio*20} pontos.\n')
            else:
                resposta_errada_mÃ©dio+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')

            print('PERGUNTA 2/10\nQuem escreveu a obra "Dom Casmurro"?\n',
            'a) JosÃ© de Alencar\n',
            'b) Clarice Lispector\n',
            'c) Machado de Assis\n',
            'd) Graciliano Ramos')
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'c':
                resposta_certa_mÃ©dio+=1
                print(f'\nâœ… CORRETO! +20 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_mÃ©dio*20} pontos.\n')
            else:
                resposta_errada_mÃ©dio+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')

            print('PERGUNTA 3/10\nQual Ã© o menor planeta do sistema solar?\n',
            'a) Saturno\n',
            'b) Terra\n',
            'c) JÃºpiter\n',
            'd) MercÃºrio')
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'd':
                resposta_certa_mÃ©dio+=1
                print(f'\nâœ… CORRETO! +20 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_mÃ©dio*20} pontos.\n')
            else:
                resposta_errada_mÃ©dio+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')

            print('PERGUNTA 4/10\nEm que ano ocorreu a RevoluÃ§Ã£o Francesa?\n',
            'a) 1492\n',
            'b) 1789\n',
            'c) 1815\n',
            'd) 1914')
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'b':
                resposta_certa_mÃ©dio+=1
                print(f'\nâœ… CORRETO! +20 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_mÃ©dio*20} pontos.\n')
            else:
                resposta_errada_mÃ©dio+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')

            print('PERGUNTA 5/10\nQual Ã© a capital do CanadÃ¡?\n',
            'a) Toronto\n',
            'b) Vancouver\n',
            'c) Montreal\n',
            'd) Ottawa')
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'd':
                resposta_certa_mÃ©dio+=1
                print(f'\nâœ… CORRETO! +20 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_mÃ©dio*20} pontos.\n')
            else:
                resposta_errada_mÃ©dio+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')

            print('PERGUNTA 6/10\nQuem foi o primeiro homem a pisar na Lua?\n',
            'a) Yuri Gagarin\n',
            'b) Buzz Aldrin\n',
            'c) Neil Armstrong\n',
            'd) Alan Shepard')
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'c':
                resposta_certa_mÃ©dio+=1
                print(f'\nâœ… CORRETO! +20 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_mÃ©dio*20} pontos.\n')
            else:
                resposta_errada_mÃ©dio+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')

            print('PERGUNTA 7/10\nQual Ã© o idioma oficial da SuÃ­Ã§a?\n',
            'a) AlemÃ£o\n',
            'b) FrancÃªs\n',
            'c) Italiano\n',
            'd) Todas as alternativas')
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'd':
                resposta_certa_mÃ©dio+=1
                print(f'\nâœ… CORRETO! +20 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_mÃ©dio*20} pontos.\n')
            else:
                resposta_errada_mÃ©dio+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')

            print('PERGUNTA 8/10\nQual Ã© o nome do processo de transformaÃ§Ã£o da Ã¡gua em vapor?\n',
            'a) EvaporaÃ§Ã£o\n',
            'b) SublimaÃ§Ã£o\n',
            'c) CondensaÃ§Ã£o\n',
            'd) FusÃ£o')
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'a':
                resposta_certa_mÃ©dio+=1
                print(f'\nâœ… CORRETO! +20 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_mÃ©dio*20} pontos.\n')
            else:
                resposta_errada_mÃ©dio+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')

            print('PERGUNTA 9/10\nQual Ã© a moeda oficial do JapÃ£o?\n',
            'a) Yuan\n',
            'b) Iene\n',
            'c) Won\n',
            'd) DÃ³lar')
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'b':
                resposta_certa_mÃ©dio+=1
                print(f'\nâœ… CORRETO! +20 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_mÃ©dio*20} pontos.\n')
            else:
                resposta_errada_mÃ©dio+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')

            print('PERGUNTA 10/10\nQuem pintou o teto da Capela Sistina?\n',
            'a) Michelangelo\n',
            'b) Leonardo da Vinci\n',
            'c) Rafael\n',
            'd) Donatello')
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'a':
                resposta_certa_mÃ©dio+=1
                print(f'\nâœ… CORRETO! +20 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_mÃ©dio*20} pontos.\n')
            else:
                resposta_errada_mÃ©dio+=1
                print(f'Erro! Sem pontuaÃ§Ã£o\n')
                print('...\n')
            print('=='*30)
            print('RESULTADO FINAL')
            print('=='*30)
            print(f'Nome: {nome}\n',
            f'Acertos: {resposta_certa_mÃ©dio}/10\n',
            f'Erros: {resposta_errada_mÃ©dio}/10\n',
            f'PontuaÃ§Ã£o final: {resposta_certa_mÃ©dio*20}')
            if resposta_certa_mÃ©dio*20==20:
                print(f'ClassificaÃ§Ã£o:\033[93mâ˜…\033[10m TransiÃ§Ã£o\n')
            elif resposta_certa_mÃ©dio*20==40:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸ\033[20m Insuficiente')
            elif resposta_certa_mÃ©dio*20==60:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸâ˜…\033[30m Regular\n')
            elif resposta_certa_mÃ©dio*20==80:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸðŸŒŸ\033[40m Mediano\n')
            elif resposta_certa_mÃ©dio*20==100:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸðŸŒŸâ˜…\033[50m Bom\n')
            elif resposta_certa_mÃ©dio*20==120:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸðŸŒŸðŸŒŸ\033[60m Muito Bom\n')
            elif resposta_certa_mÃ©dio*20==140:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸðŸŒŸðŸŒŸâ˜…\033[70m Ã“timo\n')
            elif resposta_certa_mÃ©dio*20==160:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸðŸŒŸðŸŒŸðŸŒŸ\033[80m Excelente\n')
            elif resposta_certa_mÃ©dio*20==180:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸðŸŒŸðŸŒŸðŸŒŸâ˜…\033[90m Elite\n')
            elif resposta_certa_mÃ©dio*20==200:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸðŸŒŸðŸŒŸðŸŒŸðŸŒŸ\033[77m Mestre\n')
            else:
                print('ClassificaÃ§Ã£o: Sem estrela ðŸ˜‹ Estude mais\n')
                
        elif escolha_de_jogo==3:# DifÃ­cil ronda1
            print('=='*30)
            print(f'{'MODO DIFÃCIL - 10 PERGUNTAS':^30}')
            print('=='*30)
            
            print('PERGUNTA 1/10\nQual Ã© o nome do tratado que encerrou oficialmente a Primeira Guerra Mundial?\n',
            'a) Tratado de Viena\n',
            'b) Tratado de Tordesilhas\n',
            'c) Tratado de Versalhes\n',
            'd) Tratado de Paris')
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'c':
                resposta_certa_difÃ­cil+=1
                print(f'\nâœ… CORRETO! +30 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_difÃ­cil*30} pontos.\n')
            else:
                resposta_errada_difÃ­cil+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')

            print('PERGUNTA 2/10\nQuem foi o matemÃ¡tico que formulou o Ãºltimo teorema que sÃ³ foi provado em 1994?\n',
            'a) Isaac Newton\n',
            'b) Pierre de Fermat\n',
            'c) Carl Gauss\n',
            'd) RenÃ© Descartes')
            
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'b':
                resposta_certa_difÃ­cil+=1
                print(f'\nâœ… CORRETO! +30 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_difÃ­cil*30} pontos.\n')
            else:
                resposta_errada_difÃ­cil+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')

            print('PERGUNTA 3/10\nQual Ã© o nome da partÃ­cula subatÃ´mica responsÃ¡vel pela forÃ§a nuclear forte?\n',
            'a) ElÃ©tron\n',
            'b) GlÃºon\n',
            'c) Neutrino\n',
            'd) Quark')
            
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'b':
                resposta_certa_difÃ­cil+=1
                print(f'\nâœ… CORRETO! +30 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_difÃ­cil*30} pontos.\n')
            else:
                resposta_errada_difÃ­cil+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')

            print('PERGUNTA 4/10\nQual paÃ­s tem a maior reserva comprovada de petrÃ³leo do mundo?\n',
            'a) ArÃ¡bia Saudita\n',
            'b) CanadÃ¡\n',
            'c) IrÃ£\n',
            'd) Venezuela')
            
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'd':
                resposta_certa_difÃ­cil+=1
                print(f'\nâœ… CORRETO! +30 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_difÃ­cil*30} pontos.\n')
            else:
                resposta_errada_difÃ­cil+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')

            print('PERGUNTA 5/10\nQuem compÃ´s a Ã³pera "O Barbeiro de Sevilha"?\n',
            'a) Rossini\n',
            'b) Verdi\n',
            'c) Mozart\n',
            'd) Beethoven')
            
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'a':
                resposta_certa_difÃ­cil+=1
                print(f'\nâœ… CORRETO! +30 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_difÃ­cil*30} pontos.\n')
            else:
                resposta_errada_difÃ­cil+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')

            print('PERGUNTA 6/10\nQual Ã© o nome da teoria que unifica a relatividade geral com a mecÃ¢nica quÃ¢ntica?\n',
            'a) Teoria das Cordas\n',
            'b) Teoria do Caos\n',
            'c) Teoria da Relatividade Restrita\n',
            'd) Teoria da EvoluÃ§Ã£o')
            
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'a':
                resposta_certa_difÃ­cil+=1
                print(f'\nâœ… CORRETO! +30 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_difÃ­cil*30} pontos.\n')
            else:
                resposta_errada_difÃ­cil+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')

            print('PERGUNTA 7/10\nQual Ã© a capital do CazaquistÃ£o?\n',
            'a) Almaty\n',
            'b) Astana\n',
            'c) Tashkent\n',
            'd) Baku')
            
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'b':
                resposta_certa_difÃ­cil+=1
                print(f'\nâœ… CORRETO! +30 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_difÃ­cil*30} pontos.\n')
            else:
                resposta_errada_difÃ­cil+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')

            print('PERGUNTA 8/10\nQual filÃ³sofo escreveu "CrÃ­tica da RazÃ£o Pura"?\n',
            'a) Kant\n',
            'b) Hegel\n',
            'c) Nietzsche\n',
            'd) Rousseau')
            
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'a':
                resposta_certa_difÃ­cil+=1
                print(f'\nâœ… CORRETO! +30 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_difÃ­cil*30} pontos.\n')
            else:
                resposta_errada_difÃ­cil+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')

            print('PERGUNTA 9/10\nQual Ã© o nome da missÃ£o espacial que levou o primeiro robÃ´ a pousar em Marte?\n',
            'a) Curiosity\n',
            'b) Opportunity\n',
            'c) Sojourner\n',
            'd) Spirit')
            
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'c':
                resposta_certa_difÃ­cil+=1
                print(f'\nâœ… CORRETO! +30 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_difÃ­cil*30} pontos.\n')
            else:
                resposta_errada_difÃ­cil+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')

            print('PERGUNTA 10/10\nQual Ã© o nome da estrutura cerebral associada Ã  formaÃ§Ã£o de memÃ³rias?\n',
            'a) Hipocampo\n',
            'b) AmÃ­gdala\n',
            'c) HipotÃ¡lamo\n',
            'd) TÃ¡lamo')
            
            resposta=str(input('Sua resposta: ')).strip().lower()
            if resposta == 'a':
                resposta_certa_difÃ­cil+=1
                print(f'\nâœ… CORRETO! +30 pontos\nPontuaÃ§Ã£o atual: {resposta_certa_difÃ­cil*30} pontos.\n')
            else:
                resposta_errada_difÃ­cil+=1
                print(f'\nErro! Sem pontuaÃ§Ã£o\n')
            print('...\n')
            print('=='*30,'\n')
            print('RESULTADO FINAL')
            print('=='*30)
            print(f'Nome: {nome}\n',
            f'Acertos: {resposta_certa_difÃ­cil}/10\n',
            f'Erros: {resposta_errada_difÃ­cil}/10\n',
            f'PontuaÃ§Ã£o final: {resposta_certa_difÃ­cil*30}')
            if resposta_certa_difÃ­cil*30==30:
                print(f'ClassificaÃ§Ã£o:\033[93mâ˜…\033[56m AvanÃ§ado\n')
            elif resposta_certa_difÃ­cil*30==60:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸ\033[13m Fraco')
            elif resposta_certa_difÃ­cil*30==90:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸâ˜…\033[90m Regular\n')
            elif resposta_certa_difÃ­cil*30==120:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸðŸŒŸ\033[80m Bom\n')
            elif resposta_certa_difÃ­cil*30==150:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸðŸŒŸâ˜…\033[70m Muito Bom\n')
            elif resposta_certa_difÃ­cil*30==180:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸðŸŒŸðŸŒŸ\033[60m Ã“timo\n')
            elif resposta_certa_difÃ­cil*30==210:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸðŸŒŸðŸŒŸâ˜…\033[50m Excelente\n')
            elif resposta_certa_difÃ­cil*30==240:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸðŸŒŸðŸŒŸðŸŒŸ\033[40m Elite\n')
            elif resposta_certa_difÃ­cil*30==270:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸðŸŒŸðŸŒŸðŸŒŸâ˜…\033[30m Mestre\n')
            elif resposta_certa_difÃ­cil*30==300:
                print(f'ClassificaÃ§Ã£o:\033[93mðŸŒŸðŸŒŸðŸŒŸðŸŒŸðŸŒŸ\033[20m LendÃ¡rio ðŸ†\n')
            else:
                print('ClassificaÃ§Ã£o: Sem estrela ðŸ˜‹ Estude mais\n')
        continuar=str(input('Quer continuar[s/n]: ')).lower().strip()
        print('=='*30)
        if continuar=='s':
            resposta_certa_fÃ¡cil=resposta_errada_fÃ¡cil=resposta_certa_mÃ©dio=resposta_errada_mÃ©dio=resposta_certa_difÃ­cil=resposta_errada_difÃ­cil=0
        else:
            print('\nObrigado por jogar! AtÃ© a prÃ³xima! ðŸŽ®')
            break 
    else:
        print('Obrigado, volte quando quiser!')
        break       
print('=='*30)
     
    


