PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "username" NOT NULL UNIQUE, "password" NOT NULL);
COMMIT;