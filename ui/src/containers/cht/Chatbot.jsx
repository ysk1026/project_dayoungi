import React, { Component } from 'react';
import axios from  'axios';
import ChatBot from 'react-simple-chatbot';
   
// 6번의 질문을 한다고 치면
// 6번 하면 됨
// 근데 뽀대 안남

// -> use effect -> 

export default function Chatbot(props) {
    const config = {
      width: "600px",
      height: "700px"
    };
    const steps = [
        //서비스선택
        { 
            id: '0',
            message: "배우의 성별은 어떻게 됩니까?",
            trigger: "1"
        },

        {
            id: '1',
            options: [
                {value: 1, label: '배우는 남자입니다', trigger: '2' },
                {value: 2, label: '배우는 여자입니다', trigger: '2'},
                {value: 3, label: '잘 모르겠습니다', trigger: '2'},
            ],
        },
        {
            id: '2',
            message: "배우의 나이는 어떻게 됩니까?",
            trigger: "3"
        },
        {
            id: '3',
            user: true,
            trigger: '4',
        },
        {
            id: '4',
            message: "배우는 가명이 있습니까?",
            trigger: '5',
        },
        {
            id: '5',
            options: [
                {value: 1, label: '예 가명이 있습니다', trigger: '6' },
                {value: 2, label: '아니요 본명으로 활동 중입니다', trigger: '6'},
                {value: 3, label: '잘 모르겠습니다', trigger: '6'},
            ]
        },
        {
            id: '6',
            message: '종교가 있습니까?',
            trigger: '7',
        },
        {
            id: '7',
            options: [
                {value: 1, label: '예 종교가 있습니다', trigger: '8' },
                {value: 2, label: '아니요 종교가 없습니다', trigger: '8'},
                {value: 3, label: '잘 모르겠습니다', trigger: '8'},
            ]
        },
        {
            id: '8',
            message: '소속사가 있습니까?',
            trigger: '9'
        },
        {
            id: '9',
            options: [
                {value: 1, label: '예 소속사가 있습니다', trigger: '10' },
                {value: 2, label: '아니요 소속사가 없습니다', trigger: '10'},
            ] 
        },
        {
            id: '10',
            message: '자녀가 있습니까?',
            trigger: '11',
        },
        {
            id: '11',
            options: [
                {value: 1, label: '예 있습니다', trigger: '12' },
                {value: 2, label: '아니요 없습니다', trigger: '12'},
            ] 
        },
        {
            id: '12',
            message: '데뷔년도는 몇년도 입니까?',
            trigger: '13',
        },
        {
            id: '13',
            user: true,
            trigger: '14',
        },
        {
            id: '14',
            message: "다시 하시겠습니까?",
            trigger: '15',
        },
        {
            id: '15',
            options: [
                {value: 1, label: '예 다시하겠습니다', trigger: '1' },
                {value: 2, label: '아니요 끝내겠습니다', trigger: '16'},
            ] 
        },
        {
            id: '16',
            message: "수고 하셨습니다"
        },
    ]
    
    return <ChatBot steps={steps} {...config} style={{"border": "1px solid black"}}/>;
   }