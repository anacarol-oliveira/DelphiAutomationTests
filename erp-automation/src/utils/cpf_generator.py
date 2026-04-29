import random

def gerar_cpf():
    nums = [random.randint(0, 9) for _ in range(9)]

    for _ in range(2):
        soma = sum(v * ((len(nums) + 1) - i) for i, v in enumerate(nums))
        dig = 11 - (soma % 11)
        nums.append(0 if dig > 9 else dig)

    return ''.join(map(str, nums))
