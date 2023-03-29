#SQLlite does not use this, but it is nifty reference for creating models

CREATE TABLE Members (
	user_id SERIAL PRIMARY KEY,
	firstName VARCHAR(50) NOT NULL,
	lastName VARCHAR(50) NOT NULL,
	email VARCHAR(50) UNIQUE NOT NULL,
	dob DATE NOT NULL,
	hometown VARCHAR(50),
	gender CHAR(1),
	password VARCHAR(50)
);

CREATE TABLE Friends (
	follower INT,
	target INT,
	since DATE,
	PRIMARY KEY (follower, target),
  FOREIGN KEY (follower) REFERENCES Members(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (target) REFERENCES Members(user_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Albums (
  album_id SERIAL PRIMARY KEY,
  name VARCHAR(50),
  owner INT,
  created DATE,
  FOREIGN KEY (owner) REFERENCES Members(user_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Photos (
  photo_id SERIAL PRIMARY KEY,
  album_id INTEGER NOT NULL,
  caption TEXT, 
  data BYTEA,
  FOREIGN KEY (album_id) REFERENCES Album(album_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Likes (
  user_id INT,
  photo_id INT,
  PRIMARY KEY (user_id, photo_id),
  FOREIGN KEY (user_id) REFERENCES Members(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (photo_id) REFERENCES Photo(photo_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Tags (
  tag_id SERIAL PRIMARY KEY,
  word TEXT NOT NULL,
  photo_id INTEGER NOT NULL,
  FOREIGN KEY (photo_id) REFERENCES Photo (photo_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Comments (
  comment_id SERIAL PRIMARY KEY,
  content TEXT,
  user_id INT,
  photo_id INT,
  created DATE,
  FOREIGN KEY (user_id) REFERENCES Members(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (photo_id) REFERENCES Photo(photo_id) ON DELETE CASCADE ON UPDATE CASCADE
);

#Search a user by first name
SELECT * FROM Members
WHERE firstName LIKE '%John%';

#Search a user by last name
SELECT * FROM Members
WHERE lastName LIKE '%Doe%';

#Search a user by both
SELECT * FROM Members
WHERE firstName LIKE '%John%' AND lastName LIKE '%Doe%';

#Get all albums for a user
SELECT * FROM Albums
JOIN Members ON Albums.owner = Members.user_id
WHERE Members.user_id = 123;

#Get all photos from an album
SELECT * FROM Photos
JOIN Albums ON Photos.album = Albums.album_id
WHERE Albums.album_id = 123;

#Get all the photos with a given tag
SELECT *
FROM Photos
JOIN Tags ON Photos.photo_id = Tags.photo_id
WHERE Tags.word = 'beach';

#Get all the photos with a given tag for one user(Ex. 1)
SELECT *
FROM Photos
JOIN Tags ON Photos.photo_id = Tags.photo_id
JOIN Albums ON Photos.album_id = Albums.album_id
JOIN Members ON Albums.owner = Members.user_id
WHERE Tags.word = 'beach' AND Members.user_id = 1;

#Get the total number of likes for a given photo
SELECT COUNT(*) as total_likes
FROM Likes
WHERE photo_id = photo_id;

#Get the most popular tags
SELECT word, COUNT(*) AS score
FROM Tags
GROUP BY word
ORDER BY score DESC;

#Search for users by the comment 
SELECT Members.*
FROM Members
JOIN Comments ON Members.user_id = Comments.user_id
WHERE Comments.content = 'search_text'
ORDER BY Comments.created DESC;

#Check Email
SELECT COUNT(email) 
FROM Members 
WHERE email = ‘[inputted email]’;

#Create User
INSERT INTO Members (firstName, lastName, email, DOB, hometown, gender, password)
VALUES ('John', 'Doe', 'johndoe@example.com', '1990-01-01', 'New York City', 'Male', 'coolHash');

#Create Album
INSERT INTO Albums (name, owner, created)
VALUES ('Vacation Photos', 1, '2022-08-01');

#Create Photo
INSERT INTO Photos (album_id, caption, photoPath)
VALUES (1, 'At the beach', 'filepath');

#Add Friend
INSERT INTO Friends (follower, target, since)
VALUES (1, 2, '2022-02-28 10:30:00');

#Leaving Comments
INSERT INTO Comments (content, user_id, photo_id, created) VALUES (“example”, 1, 1, '2022-08-01');

#Adding Likes
INSERT INTO Likes (user_id, photo_id) VALUES (1, 1);

#Show Friends
SELECT follower FROM friends WHERE target = “current_user_id”;

#Search for Friends vis User_id
SELECT follower FROM friends WHERE target = “searched_user_id”;

#Generate top 10 contributors
SELECT Members.user_id, Members.firstName, Members.lastName, 
  COUNT(DISTINCT Comments.comment_id) as comment_count,
  COUNT(DISTINCT Photos.photo_id) as photo_count,
  COUNT(DISTINCT Comments.comment_id) + COUNT(DISTINCT AlbumPhotos.photo_id) as contribution_score
FROM Members
LEFT JOIN Comments ON Members.user_id = Comments.user_id
LEFT JOIN Photos ON Photos.album_id = ANY(SELECT album_id FROM Albums WHERE owner = Members.user_id)
LEFT JOIN Photos as AlbumPhotos ON AlbumPhotos.album_id IN (SELECT album_id FROM Albums WHERE owner = Members.user_id)
GROUP BY Members.user_id
ORDER BY contribution_score DESC
LIMIT 10;

#Get Contribution Score
SELECT Members.user_id, Members.firstName, Members.lastName, 
  COUNT(DISTINCT Comments.comment_id) as comment_count,
  COUNT(DISTINCT Photos.photo_id) as photo_count,
  COUNT(DISTINCT Comments.comment_id) + COUNT(DISTINCT AlbumPhotos.photo_id) as contribution_score
FROM Members
LEFT JOIN Comments ON Members.user_id = Comments.user_id
LEFT JOIN Photos ON Photos.album_id = ANY(SELECT album_id FROM Albums WHERE owner = Members.user_id)
LEFT JOIN Photos as AlbumPhotos ON AlbumPhotos.album_id IN (SELECT album_id FROM Albums WHERE owner = Members.user_id)
WHERE Members.user_id = [User_ID to search]
GROUP BY Members.user_id;

#Logging in
SELECT COUNT(*)
FROM Members
WHERE Members.email = 'email' AND Members.password = 'password';

#Homescreen Photos
SELECT *
FROM photos
JOIN albums ON photos.album_id = albums.album_id
JOIN Members on albums.owner = Members.user_id 
join friends on friends.follower = Members.user_id
WHERE friends.target = [user_id]
ORDER BY albums.create DESC;

#Display Album Photos
SELECT photo_id, path
FROM photos
WHERE album_id = (requested album_id);

#Display Albums
SELECT album_id, name
FROM albums
WHERE owner = (user_id);

#Edit Album
UPDATE Albums SET name = 'updated name' WHERE album_id = 1;

#Edit Photo
UPDATE Photos SET caption = 'updated caption' WHERE photo_id = 1;

#Delete Album
DELETE FROM Albums WHERE album_id = 1;

#Delete Photos
DELETE FROM Photos WHERE photo_id = 1;

#Viewing a user’s photos by tag name
SELECT *
FROM photos
JOIN tags ON photos.photo_id = tags.photo_id
JOIN albums ON photos.album_id = albums.album_id
JOIN Members on albums.owner = Members.user_id 
WHERE tags.word = '#[search tag]' AND Members.user_id = [searched user];

#Viewing all photos by tag name
SELECT *
FROM photos
JOIN tags ON photos.photo_id = tags.photo_id
WHERE Tags.word = '#[search tag]';

#Viewing the most popular (10) tags
SELECT word, COUNT(*) AS score
FROM Tags
GROUP BY word
ORDER BY score DESC
LIMIT 10;

#Photo Search
#Note: (can search up to 3 tags. If less, simply set the excess searches to the ones already listed)
SELECT photos.photo_id
FROM photos
JOIN tags t1 ON t1.photo_id = photos.photo_id
JOIN tags t2 ON t2.photo_id = photos.photo_id
JOIN tags t3 ON t3.photo_id = photos.photo_id
WHERE t1.word = '#[search1]'
AND t2.word = '#[search2]'
AND t3.word = '#[search3]';

#Removing Likes
DELETE FROM Likes WHERE user_id = 1 AND photo_id = 1;

#Comment Search
SELECT Members.firstName, Members.lastName, COUNT(*) as comment_count
FROM Comments
JOIN Members ON Members.user_id = Comments.user_id
WHERE Comments.content = '[search text]'
GROUP BY Members.user_id
ORDER BY comment_count DESC;
 
#Friend recommendations
SELECT u.user_id, COUNT(*) as mutual_friend_count
FROM Friends AS f1
JOIN Friends AS f2 ON f1.target = f2.follower
JOIN Friends AS fof ON f2.target = fof.follower
JOIN Friends AS mutual ON f1.follower = mutual.follower AND fof.target = mutual.target
JOIN Members u ON fof.target = u.user_id
AND fof.target NOT IN (SELECT target FROM Friends WHERE follower = 1)
AND fof.target != 1
GROUP BY u.user_id, fof.target
ORDER BY mutual_friend_count DESC;

