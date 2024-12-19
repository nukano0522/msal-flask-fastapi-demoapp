-- データベースの設定 (必要に応じて)
CREATE DATABASE mydatabase CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE mydatabase;

-- テーブルの作成
CREATE TABLE organizations (
    id INT PRIMARY KEY,
    organization VARCHAR(100) CHARACTER SET utf8mb4
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- データの投入
INSERT INTO organizations (id, organization) VALUES(1, 'Org1'),(2, 'Org2'),(3, 'Org3');

-- テーブルの作成
CREATE TABLE member (
    id INT PRIMARY KEY,
    member_name VARCHAR(100) CHARACTER SET utf8mb4,
    organization_id INT
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- データの投入
INSERT INTO member (id, member_name, organization_id) VALUES (1, 'Suzuki Ichiro', 1),(2, 'Sato Jiro', 1),(5, 'Stranger', 2);

select organization, member_name from member t1 inner join organizations t2 on t1.organization_id=t2.id where t2.id=1;