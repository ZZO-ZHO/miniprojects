﻿using Bogus;
using FakeIotDeviceApp.Models;
using MahApps.Metro.Controls;
using MahApps.Metro.Controls.Dialogs;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using uPLibrary.Networking.M2Mqtt;

namespace FakeIotDeviceApp
{
    /// <summary>
    /// MainWindow.xaml에 대한 상호 작용 논리
    /// </summary>
    public partial class MainWindow : MetroWindow
    {
        Faker<SensorInfo> FakeHomeSensor = null;    // 가짜 스마트홈 센서값 변수
        
        MqttClient client;
        Thread MqttThread {get;set;}

        public MainWindow()
        {
            InitializeComponent();

            InitFakeData();
        }

        private void InitFakeData()
        {
            var Rooms = new[] { "Bed", "Bath", "Living", "Dining" };

            FakeHomeSensor = new Faker<SensorInfo>()
                .RuleFor(s => s.Home_Id, "D101H704")                         // 임의로 정한 스마트홈ID
                .RuleFor(s => s.Room_Name, f => f.PickRandom(Rooms))         // 실핼할떄마다 방이름 계속 변경
                .RuleFor(s => s.Sensing_DateTime, f => f.Date.Past(0))       // 현재시각 생성
                .RuleFor(s => s.Temp, f => f.Random.Float(20.0f, 30.0f))     // 20~30도사이의 온도값 생성
                .RuleFor(s => s.Humid, f => f.Random.Float(40.0f, 64.0f));   // 40~64% 사이의 습도값
        }

        private async void BtnConnect_Click(object sender, RoutedEventArgs e)
        {
            if (string.IsNullOrEmpty(TxtMqttBrokerIp.Text))
            {
                await this.ShowMessageAsync("오류","브로커 IP를 입력하세요.");
                return;
            }

            // 브로커IP로 접속
            ConnectMqttBroker();

            // 하위로직을 무한반복
            StartPublish();

        }

        private void StartPublish()
        {
            MqttThread = new Thread(() =>
            {
                while (true)
                {
                    // 가짜 스마트홈 센서값 생성
                    SensorInfo Info = FakeHomeSensor.Generate();
                    Debug.WriteLine($"{Info.Home_Id} / {Info.Room_Name} / {Info.Sensing_DateTime} / {Info.Temp}");
                    // 센서값 MQTT브로커에 전송 (Publish)


                    // RtbLog에 출력
                    

                    // 1초동안 대기
                    Thread.Sleep(1000);
                }
            });
            MqttThread.Start();
        }

        private void ConnectMqttBroker()
        {
            client = new MqttClient(TxtMqttBrokerIp.Text);
            client.Connect("SmartHomeDev");     // publish client ID를 지정 
        }

        private void MetroWindow_Closing(object sender, System.ComponentModel.CancelEventArgs e)
        {
            if (client != null && client.IsConnected == true)
            {
                client.Disconnect();    // 접속을 끊어줌
            }

            if(MqttThread != null)
            {
                MqttThread.Abort();     // 이부분이 없으면 프로그램 종료이후에도 메모리에 남아있음
            }
        }
    }
}
