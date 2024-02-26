import axios from "axios";

const URL = 'https://test.it-kyzyl.ru/api/'

export async function mylogin(userName, passWord) {
  let data = {
    'username': userName,
    'password': passWord
  };
  try {
    let resp = await fetch(URL + 'token/', {
      method: 'POST',
      // credentials: 'omit',
      headers: {
        'Content-Type': 'application/json;charset=utf-8'
      },
      body: JSON.stringify(data)
    })
    let result = await resp.json();
    return result;
  }
  catch (e) {
    console.log('Error: ' + e.message);
  }
}

export async function getCategoryList(token) {
  try {
    let resp = await fetch(URL + 'category/', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
    let result = await resp.json();
    return result;
  } catch (e) {
    console.log('Error: ' + e.message);
  }
}

export async function getCourseList(token) {
  try {
    let resp = await fetch(URL + 'course/', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
    let result = await resp.json();
    return result;
  } catch (e) {
    console.log('Error: ' + e.message);
  }
}


// ///////////////////////////////////// axios //////////////////////
const instance = axios.create({
  withCredentials: true,
  baseURL: 'https://test.it-kyzyl.ru/api/',
});

export async function axlogin(username, password) {
  try {
    return await instance.post(
      'token/',
      {
        'username': username,
        'password': password
      },
      {
        headers: {
          "Content-type": "application/json; charset=UTF-8"
        }
      });
  } catch (e) {
    console.log(e);
  };
}

export async function axGetCategoryList(token) {
  try {
    return await instance.get(
      'category/',
      {
        headers: {
          "Content-type": "application/json; charset=UTF-8",
          'Authorization': `Bearer ${token}`
        }
      });
  } catch (e) {
    console.log(e);
  };
}

export async function axGetCourseList(token) {
  try {
    return await instance.get(
      'course/',
      {
        headers: {
          "Content-type": "application/json; charset=UTF-8",
          'Authorization': `Bearer ${token}`
        }
      });
  } catch (e) {
    console.log(e);
  };
}