# @me API仕様

## 詳細、最新情報は"https://APIROOT:PORT/docs"または、"https://APIROOT:PORT/redoc"を参照されたし。

## Auth

## Users

### POST /users/check

ユーザーログイン時に呼び出され、ユーザーがアプリ側DBに存在するかどうかの確認  
アプリ側がユーザーの情報を持っている場合、動作なし  
持っていなかった場合、新規登録
最後の外部プロバイダー同期から6時間以上たっていれば、タスク・カレンダーの再同期

## Calenders

### GET /calenders?date={}

指定された日付の予定を取得する

## Tasks

### GET /tasks?date={}

指定された日付のタスクを取得する

### GET /tasks/deadline

1週間以内が締め切りのタスクの一覧を取得

### GET /tasks/near

直近１週間が締め切りのタスク一覧を取得

## Sync

### POST /sync

登録されているプロバイダーから情報を一括取得


# For Develop

Discordより引用
```
ここから秘密鍵落として「firebase-adminsdk.json」っていう名前でappディレクトリ直下（at-me/api/appfirebase-adminsdk.json）においてください
そういえばgitignoreにしてた
```

https://console.firebase.google.com/project/PROJECTROOT/settings/serviceaccounts/adminsdk