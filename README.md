# Tic-Tac-Toe Over TCP

This project implements a simple Tic-Tac-Toe game where a server and a client communicate over a TCP connection. The server and client alternate turns to place their marks (O and X respectively) on the board. The game continues until a player wins or the board is full, resulting in a tie.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [How It Works](#how-it-works)
  - [Setting Up the Server](#setting-up-the-server)
  - [Setting Up the Client](#setting-up-the-client)
  - [Game Loop](#game-loop)
  - [Sending and Receiving Data](#sending-and-receiving-data)
  - [Board Display](#board-display)
- [Error Handling](#error-handling)
- [Conclusion](#conclusion)

## Overview

The project demonstrates how to create a client-server application using Python's socket module. The server hosts the game, while the client connects to the server to play. The game board is displayed in the console, and players take turns to input their moves.

## Features

- **TCP Communication**: Ensures reliable and ordered communication between server and client.
- **Turn-based Gameplay**: Server and client take turns to play.
- **Win/Tie Detection**: Checks for win conditions and ties after each move.
- **Error Handling**: Handles invalid moves and connection issues gracefully.

## Requirements

- Python 3.x
- Basic understanding of sockets and TCP/IP protocol

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/tictactoe-tcp.git
   cd tictactoe-tcp
