import signupUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return signupUser(firstName, lastName)
    .then((user) => uploadPhoto(fileName).then((photo) => {
      console.log(`${user} ${photo}`);
    }))
    .catch((error) => console.log(error.toString()));
}
