#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Structure to represent the state of the jugs
typedef struct State {
    int jug1;
    int jug2;
} State;

// Function to check if the goal state is reached
bool isGoalState(State state, int goal) {
    return state.jug1 == goal || state.jug2 == goal;
}

// Function to print a state
void printState(State state) {
    printf("(%d, %d)\n", state.jug1, state.jug2);
}

// Depth First Search (DFS)
void DFS(int capacity1, int capacity2, int goal) {
    printf("\nDFS Solution:\n");
    State stack[100];
    int top = -1;

    bool visited[capacity1 + 1][capacity2 + 1];
    for (int i = 0; i <= capacity1; i++) {
        for (int j = 0; j <= capacity2; j++) {
            visited[i][j] = false;
        }
    }

    State start = {0, 0};
    stack[++top] = start;

    while (top >= 0) {
        State current = stack[top--];

        if (visited[current.jug1][current.jug2]) {
            continue;
        }

        visited[current.jug1][current.jug2] = true;
        printState(current);

        if (isGoalState(current, goal)) {
            printf("Goal state reached!\n");
            return;
        }

        // Generate successors
        State successors[] = {
            {capacity1, current.jug2}, // Fill jug1
            {current.jug1, capacity2}, // Fill jug2
            {0, current.jug2},         // Empty jug1
            {current.jug1, 0},         // Empty jug2
            {current.jug1 - (capacity2 - current.jug2) >= 0 ? current.jug1 - (capacity2 - current.jug2) : 0,
             current.jug1 + current.jug2 <= capacity2 ? current.jug1 + current.jug2 : capacity2}, // Pour jug1 to jug2
            {current.jug1 + current.jug2 <= capacity1 ? current.jug1 + current.jug2 : capacity1,
             current.jug2 - (capacity1 - current.jug1) >= 0 ? current.jug2 - (capacity1 - current.jug1) : 0}  // Pour jug2 to jug1
        };

        // Push unvisited successors to stack
        for (int i = 0; i < 6; i++) {
            State next = successors[i];
            if (!visited[next.jug1][next.jug2]) {
                stack[++top] = next;
            }
        }
    }

    printf("No solution found!\n");
}

// Breadth First Search (BFS)
void BFS(int capacity1, int capacity2, int goal) {
    printf("\nBFS Solution:\n");
    State queue[100];
    int front = 0, rear = 0;

    bool visited[capacity1 + 1][capacity2 + 1];
    for (int i = 0; i <= capacity1; i++) {
        for (int j = 0; j <= capacity2; j++) {
            visited[i][j] = false;
        }
    }

    State start = {0, 0};
    queue[rear++] = start;

    while (front < rear) {
        State current = queue[front++];

        if (visited[current.jug1][current.jug2]) {
            continue;
        }

        visited[current.jug1][current.jug2] = true;
        printState(current);

        if (isGoalState(current, goal)) {
            printf("Goal state reached!\n");
            return;
        }

        // Generate successors
        State successors[] = {
            {capacity1, current.jug2}, // Fill jug1
            {current.jug1, capacity2}, // Fill jug2
            {0, current.jug2},         // Empty jug1
            {current.jug1, 0},         // Empty jug2
            {current.jug1 - (capacity2 - current.jug2) >= 0 ? current.jug1 - (capacity2 - current.jug2) : 0,
             current.jug1 + current.jug2 <= capacity2 ? current.jug1 + current.jug2 : capacity2}, // Pour jug1 to jug2
            {current.jug1 + current.jug2 <= capacity1 ? current.jug1 + current.jug2 : capacity1,
             current.jug2 - (capacity1 - current.jug1) >= 0 ? current.jug2 - (capacity1 - current.jug1) : 0}  // Pour jug2 to jug1
        };

        // Enqueue unvisited successors
        for (int i = 0; i < 6; i++) {
            State next = successors[i];
            if (!visited[next.jug1][next.jug2]) {
                queue[rear++] = next;
            }
        }
    }

    printf("No solution found!\n");
}

int main() {
    int capacity1, capacity2, goal, choice;

    printf("Enter capacity of jug1: ");
    scanf("%d", &capacity1);
    printf("Enter capacity of jug2: ");
    scanf("%d", &capacity2);
    printf("Enter the goal amount: ");
    scanf("%d", &goal);

    do {
        printf("\nMenu:\n");
        printf("1. Solve using DFS\n");
        printf("2. Solve using BFS\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                DFS(capacity1, capacity2, goal);
                break;
            case 2:
                BFS(capacity1, capacity2, goal);
                break;
            case 3:
                printf("Exiting program.\n");
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    } while (choice != 3);

    return 0;
}

