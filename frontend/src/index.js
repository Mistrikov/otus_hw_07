import {getCategoryList, getCourseList, mylogin, axlogin, axGetCategoryList, axGetCourseList} from './myfunc.js';

async function start() {
// fetch
    //let token = (await mylogin('student1', '1')).access;
    // console.log(token);
    //let categories = await getCategoryList(token);
    //console.log('Список категорий курсов');
    //console.log(categories);
    //let cources = await getCourseList(token);
    //console.log('Список курсов');
    //console.log(cources);

// axios
    let token = (await axlogin('student1', '1')).data.access;
    //console.log(token);
    let categories = (await axGetCategoryList(token)).data;
    console.log('Список категорий курсов');
    console.log(categories);
    let cources = (await axGetCourseList(token)).data;
    console.log('Список курсов');
    console.log(cources);
}

start();