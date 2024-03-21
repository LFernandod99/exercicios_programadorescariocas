




salarioCliente = float(input("Digite seu salario: R$"))

if salarioCliente >= 3000:
    print(f''' 
      ===========================
      SALARIO DO CLIENTE: {salarioCliente}
      PLANO A SER OFERTADO [PLANO ALPHA]
      ===========================
      ''')
else: 
    print(f'''
      ===========================
      SALARIO DO CLIENTE: {salarioCliente}
      PLANO A SER OFERTADO [PLANO BETA]
      ===========================
      ''')