# python-exercism

exercismというコーディング試験サイトの学習帳簿です

## Q.なぜexercismなのか

* webサイトが英語なので英語になれるため

* 試験内容が、付属の自動テストにパスすることを前提に作られているため、テスト駆動開発の形式で進められる

* 多くのコーディング試験サービスでは、独学用途だろうとgithubにpushすることは勧められないが、exercismでは寛容と聞いたことがある(もし指摘されたらリポジトリは削除します)

## exercismの実行コマンド

~~~
docker-compose run --rm python-exercism poetry run python ghost-gobble-arcade-game/arcade_game.py

docker-compose run --rm python-exercism poetry run pytest ghost-gobble-arcade-game/arcade_game_test.py
~~~


## 以下開発者向け

~~~
# コンテナにアタッチしたい場合
docker exec -it udemy-python bash
# poetryを実行する場合
docker-compose run -rm udemy-python poetry run [コマンド名]
~~~

以下の2つのコマンドを使うとpoetryでパスが仮装環境用に変更してくれているのがわかる
~~~
env | grep PATH
poetry run env |grep PATH
~~~

現在はリンターはruffで設定されているが、別のリンターにする場合はvscodeで該当のリンターをインストールした上で以下を実行

1. vscode上でcommand + , を入力

2. default formatterと検索して、該当のリンターに変更する

定期的に以下を行うこと

~~~
docker system prune
docker volume prune
~~~