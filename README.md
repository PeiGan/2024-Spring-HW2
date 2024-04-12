# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution

Path: tokenB->tokenA->tokenE->tokenD->tokenC->tokenB

tokenB: 5.000000000000000000

tokenA: 5.655321988655321988

tokenE: 1.058315313806688639

tokenD: 2.429786260142226801

tokenC: 5.038996197252911039

tokenB: 20.042339589188176107

Final reward: 20.042339589188176107

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution

The AMM holds the constant product rule. So, if a liquidity pool with tokenA = 10 and tokenB = 10, it seems that selling 1 tokenA will give you 1 tokenB.
However, the amount you'll get is 10 - 10 * 10 / 11 $\approx$ 0.91 to hold the constant product rule. The difference is called slippage.

In Uniswap V2, the two functions `swapExactTokensForTokens` and `swapTokensForExactTokens` in the router contract both have the protection to slippage.
One specifies `amountIn` and `amountOutMin`, and the other specifies `amountInMax` and `amountOut`, to make sure the price is within the tolerence interval of users.

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

The reason behind this design is to avoid a single unit of liquidity token being too large for one to provide liquidity. If one initializes a pool with 1e-18 ETH and 1e-18 DAI, he gets 1 LP token. Then if someone donates 100 ETH and 100 DAI into the pool, one LP token worths 100 ETH + 100 DAI now. If one wants to provide liquidity, he have to provide 100 ETH and 100 DAI. However, with the initial amount of LP tokens being burned, which is 1000 LP token, even if someone donates 100 ETH and 100 DAI into the pool, 1 LP token still only worth 0.1 ETH + 0.1 DAI, which is desirable.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

The formula is to force the liquidity provider to provide liquidity at the current rate. Consider the first provider holding 1 LP token with 1 ETH + 1 DAI provided. If someone provide another 1 ETH + 2 DAI, then the pool becomes 2 ETH + 3 DAI. If the formula is not taking minimum of the ratio, say, taking maximum, then the new provider gets 2 LP, which should worth 2 ETH + 2 DAI, which is absolutely a robbery on the first provider. So, taking minimum is the most reasonable way.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution

A sandwich attack is that when you try to swap token A for token B at DEXes utilizing AMM, attackers can front-run (by higher gas fee) to change the ratio of the liquidity pool, sell it afterward your swap, and arbitrage from it. Since the attackers earn profit from it, users loses money. 

For example, User want to swap 1 ETH to DAI with ETH/DAI pool, where ETH=5, DAI=12000. (Without considering fees)

Without sandwich attack, the user get 12000 - 5 * 12000 / 6 = 2000 DAI.

With sandwich attack, attacker First sell 1 ETH for DAI in this pool, so the pool become ETH = 6, DAI = 10000, and the attacker with 2000 DAI.

Then, the user get 10000 - 6 * 10000 / 7 = 1428.57 DAI, where the pool is ETH = 7, DAI = 8571.43.

At last, the attacker swap the 2000 DAI back, so he gets 7 - 7 * 8571.43 / 10571.43 = 1.324 ETH.

In the end, the user lost ~572 DAI and the attacker earned ~.324 ETH.
