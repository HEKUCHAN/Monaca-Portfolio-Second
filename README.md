<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [もなかのポートフォリオ (Nuxt with Django RFW)](#%E3%82%82%E3%81%AA%E3%81%8B%E3%81%AE%E3%83%9D%E3%83%BC%E3%83%88%E3%83%95%E3%82%A9%E3%83%AA%E3%82%AA-nuxt-with-django-rfw)
  - [お問い合わせフォーム](#%E3%81%8A%E5%95%8F%E3%81%84%E5%90%88%E3%82%8F%E3%81%9B%E3%83%95%E3%82%A9%E3%83%BC%E3%83%A0)
  - [管理ページログイン機能](#%E7%AE%A1%E7%90%86%E3%83%9A%E3%83%BC%E3%82%B8%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3%E6%A9%9F%E8%83%BD)
  - [サイトに対してのいいね機能](#%E3%82%B5%E3%82%A4%E3%83%88%E3%81%AB%E5%AF%BE%E3%81%97%E3%81%A6%E3%81%AE%E3%81%84%E3%81%84%E3%81%AD%E6%A9%9F%E8%83%BD)
  - [スキル表示機能](#%E3%82%B9%E3%82%AD%E3%83%AB%E8%A1%A8%E7%A4%BA%E6%A9%9F%E8%83%BD)
  - [お知らせ](#%E3%81%8A%E7%9F%A5%E3%82%89%E3%81%9B)
  - [ブログ](#%E3%83%96%E3%83%AD%E3%82%B0)
  - [成果物報告ページ](#%E6%88%90%E6%9E%9C%E7%89%A9%E5%A0%B1%E5%91%8A%E3%83%9A%E3%83%BC%E3%82%B8)
  - [チップ機能（案件のお支払いや支払先が書いてあるページ）](#%E3%83%81%E3%83%83%E3%83%97%E6%A9%9F%E8%83%BD%E6%A1%88%E4%BB%B6%E3%81%AE%E3%81%8A%E6%94%AF%E6%89%95%E3%81%84%E3%82%84%E6%94%AF%E6%89%95%E5%85%88%E3%81%8C%E6%9B%B8%E3%81%84%E3%81%A6%E3%81%82%E3%82%8B%E3%83%9A%E3%83%BC%E3%82%B8)
  - [商品ページ](#%E5%95%86%E5%93%81%E3%83%9A%E3%83%BC%E3%82%B8)
- [環境構築](#%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89)
  - [開発者の開発環境](#%E9%96%8B%E7%99%BA%E8%80%85%E3%81%AE%E9%96%8B%E7%99%BA%E7%92%B0%E5%A2%83)
  - [Django](#django)
    - [1. Pipのバージョンを最新にする](#1-pip%E3%81%AE%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B3%E3%82%92%E6%9C%80%E6%96%B0%E3%81%AB%E3%81%99%E3%82%8B)
    - [2. Pipenvをインストールする](#2-pipenv%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B)
    - [3. 必要なパッケージをPipenv使ってインストール](#3-%E5%BF%85%E8%A6%81%E3%81%AA%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%82%92pipenv%E4%BD%BF%E3%81%A3%E3%81%A6%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
    - [4. Djangoのサーバーを起動](#4-django%E3%81%AE%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%82%92%E8%B5%B7%E5%8B%95)
    - [Djangoのコマンドを使う時](#django%E3%81%AE%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%82%92%E4%BD%BF%E3%81%86%E6%99%82)
  - [Nuxt.js](#nuxtjs)
    - [1. Yarnをインストール](#1-yarn%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
    - [2. 必要なライブラリーをインストール](#2-%E5%BF%85%E8%A6%81%E3%81%AA%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E3%83%BC%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
    - [3. 0.0.0.0:3000でホットリロードを提供](#3-00003000%E3%81%A7%E3%83%9B%E3%83%83%E3%83%88%E3%83%AA%E3%83%AD%E3%83%BC%E3%83%89%E3%82%92%E6%8F%90%E4%BE%9B)
  - [Nuxt.js 本番用ビルド](#nuxtjs-%E6%9C%AC%E7%95%AA%E7%94%A8%E3%83%93%E3%83%AB%E3%83%89)
  - [Nuxt.js 静的プロジェクトの生成](#nuxtjs-%E9%9D%99%E7%9A%84%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%81%AE%E7%94%9F%E6%88%90)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# もなかのポートフォリオ (Nuxt with Django RFW)

もなかのポートフォリオの作成で、高機能で便利な機能をたくさんつけることを目標にプロジェクトを始めました。

今のところつける予定の機能

## お問い合わせフォーム
- お問い合わせの情報を保存して、送信されたら管理者に向けて、メールを送信
- 毎分の送信限度を設定
- 複数の管理者にメールを送信
- お問い合わせ管理ページでメールの既読、未読を分かりやすくする
- お問い合わせが来たら通知が来るようにする

## 管理ページログイン機能
- ログイン機能をつける
- ログイン失敗制限回数をつける
- 権限の振り分けをして、できることとできないことを分ける
- 管理を複数にできるようにする

## サイトに対してのいいね機能
- いいね数を数えてくれる、これに通信制限ついたらめんどくさいからココも考え中

## スキル表示機能
- 持っているスキルを表示できる
- 管理画面から情報を更新したり、追加できるようにする
- スキルの詳細を見ることができて、そのスキルに関する記事や作品を表示する

## お知らせ
- 基本的なお知らせでページの見やすい場所に配置する
- お知らせを追加したりできるようにする
- 画像をアップロードできるようにする
- マークダウンで書けるようにする
- マークダウンの詳細ページを作成する

## ブログ
- 複数のユーザーでブログが書けるようにする
- 仮書きみたいな事ができるように書いてる内容を維持的に保存する機能
- 記事を書く場所でショートカットキーが使えるようにする
- textareaを使わずに作成する　<- 見た目重視
- ブログのサムネイルをつけれるようにする
- いいねとシェアができるようにする
- コメント機能をつける（返信はまだ考えてる）<- だいぶめんどくさい
- タグつけれるようにする

## 成果物報告ページ
- 達成したり受けた成果物や案件などの紹介を行うページ
- 追加、削除、編集できるようにする、
- マークダウンでかけて、サムネイルをつけれるようにする
- ブログとほぼ変わらない

## チップ機能（案件のお支払いや支払先が書いてあるページ）
**可能ならば**
- 有料のお金を送れるようにする
- 支払い先の記述（銀行など）
- そのページからクレジットカードでのお支払いを可能ににする（チップ）

## 商品ページ
**可能ならば**
- 簡単に言えばココナラみたいに出品できるところ

# 環境構築

## 開発者の開発環境

***Windows***
(2021年9月23日)

```
CPU: Intel Core i7-8700 3.20GHz
メモリ: 16GB 2667MHz
GPU: NVIDIA GeForce RTX2060 6GB
Windows Verion: 20H2
Python Version: Python 3.9.5
Pipenv Version: 2021.5.29
rest_framework Version: 3.12.4
```

***MacOS***
(2021年9月23日)

```
macOS: Big Sur 11.4
MacBook Pro (13-inch, 2020, Four Thunderbolt 3ports)
CPU: 2GHz クアッドコアintel Core i5
メモリ: 16GB 3733 MHz LPDDR4X
GPU: intel Iris Plus Graphics 1536 1536MB
Python 3.9.6
Pipenv Version: 2021.5.29
rest_framework Version: 3.12.4
```

## Django

環境構築はPythonが入ってる前提で進めていきます

### 1. Pipのバージョンを最新にする
```bash
$ pip install --upgrade pip
```
### 2. Pipenvをインストールする
```bash
$ pip install pipenv
```
### 3. 必要なパッケージをPipenv使ってインストール
```bash
$ pipenv install
```
ターミナルに`pipenv`と打ってインストールできているか試してください。
### 4. Djangoのサーバーを起動
```bash
# cd api
$ pipenv run python manage.py runserver
```

### Djangoのコマンドを使う時
```bash
# cd api
$ pipenv run python manage.py コマンド
```

## Nuxt.js

Node.jsをインストールしといてください。 やり方は下を参照しください 

https://github.com/hokaccha/nodebrew

### 1. Yarnをインストール
```bash
# cd web
$ npm install --global yarn
```
### 2. 必要なライブラリーをインストール
```bash
# cd web
$ yarn install
```
### 3. 0.0.0.0:3000でホットリロードを提供
```bash
# cd web
$ yarn dev
```

## Nuxt.js 本番用ビルド

```bash
# cd web
$ yarn build
$ yarn start
```

## Nuxt.js 静的プロジェクトの生成

```bash
# cd web
$ yarn generate
```