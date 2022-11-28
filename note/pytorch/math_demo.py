import torch

# 求平均
a = torch.tensor([3, 4, 5], dtype=torch.float64)
# 保持维度
b = a.mean(-1, keepdim=True)
# tensor([4.], dtype=torch.float64)
c = torch.mean(a)
# tensor(4., dtype=torch.float64)


# 求和
print('求和', a.sum())
print('求和', torch.sum(a))
# tensor([ 9., 16., 25.], dtype=torch.float64)

# 平方
print('平方值:', a.pow(2))
print('平方值:', torch.pow(a, 2))
# tensor([1.7321, 2.0000, 2.2361], dtype=torch.float64)

# 开方
print('开方', torch.sqrt(a))
print('开方', a.sqrt())

# 张量对应元素相乘
b = a
c = torch.mul(a, b)
print("元素相乘：", c)
# tensor([ 9., 16., 25.], dtype=torch.float64)

d = torch.matmul(a, b.t())
print("内积:", d)
# tensor(50., dtype=torch.float64)

# 加法
print("加：", a.add(b))
print("加：", a + b)

# 减法
print("减:", a.sub(a))
print("减:", a - a)

# 除
print("除：", a.div(b))
print("除：", a / b)