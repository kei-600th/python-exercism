def exchange_money(budget, exchange_rate):
    return budget / exchange_rate
    # 交換された通貨の値


def get_change(budget, exchanging_value):
    return budget - exchanging_value
    # 予算から交換に使われた後の残額


def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills
    # 交換所が返すことができる紙幣の総額


def get_number_of_bills(amount, denomination):
    return amount // denomination
    # 与えられた金額内で受け取ることができる紙幣の数


def get_leftover_of_bills(amount, denomination):
    return amount % denomination
    # 紙幣の額面通りに交換した後の残額


def exchangeable_value(budget, exchange_rate, spread, denomination):
    # 手数料を考慮した実際の交換レートを計算
    actual_exchange_rate = exchange_rate * (1 + spread / 100)

    # 予算を修正後の交換レートで交換して得られる外貨の額
    exchanged_currency = budget / actual_exchange_rate

    # 指定された紙幣の額面に基づいて、実際に交換できる紙幣の最大数を計算
    exchangeable_amount = (exchanged_currency // denomination) * denomination

    # 整数で結果を返す
    return int(exchangeable_amount)
