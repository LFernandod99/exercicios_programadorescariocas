vendasMes= float(input("digite o valor de vendas: R$"))
metaAtingida = 0.004
metaNaoAtingida = 0.02
comissao = 0
metaMes = 10000

if ( vendasMes >= metaMes ):
    comissao = vendasMes * metaAtingida
    print(f''' 
++++++++++++++++++++++++++++++++++++++++++++++++++
                Meta Atingida  
          
        Sua vendas foram de R${vendasMes:.2f}
        Sua comissao será de R${comissao:.2f} 
        PARABENS!!!         
++++++++++++++++++++++++++++++++++++++++++++++++++
        1''')
    
elif(vendasMes < metaMes):
    comissao = vendasMes * metaNaoAtingida
    print(f''' 
++++++++++++++++++++++++++++++++++++++++++++++++++
                Meta não Atingida  

        Sua vendas foram de R${vendasMes:.2f}
        Sua comissao será de R${comissao:.2f}  
        MELHORE !!!!        
++++++++++++++++++++++++++++++++++++++++++++++++++
        ''')   
